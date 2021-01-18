import re
import asyncio
import plistlib
from utils.parser import Parser

MIN_MACOS = 5
MAX_MACOS = 16

class macOS:
    def __init__(self, product_id):
        self.product_id = product_id

    title = ""
    version = ''
    build = ""
    packages = []


class SwScanFetcher:
    # Apple SWSCAN 서버를 접근하기 위한 헤더
    osinstall = {"User-Agent":"osinstallersetupplaind (unknown version) CFNetwork/720.5.7 Darwin/14.5.0 (x86_64)"}
    swupdate = {"User-Agent":"Software%20Update (unknown version) CFNetwork/807.0.1 Darwin/16.0.0 (x86_64)"}
    testagent = {"User-Agent":"Mozilla"}

    def __init__(self):
        self.HTTP = Parser() # 커스텀 리퀘스트 보내는 클래스 - aiohttp 사용
        self.catalog_suffix = {
            "publicseed" : "beta",
            "publicrelease" : "",
            "customerseed" : "customerseed",
            "developerseed" : "seed"
        }
        self.mac_os_names_url = {
            "8" : "mountainlion",
            "7" : "lion",
            "6" : "snowleopard",
            "5" : "leopard"
        }
        self.version_names = {
            "tiger" : "10.4",
            "leopard" : "10.5",
            "snow leopard" : "10.6",
            "lion" : "10.7",
            "mountain lion" : "10.8",
            "mavericks" : "10.9",
            "yosemite" : "10.10",
            "el capitan" : "10.11",
            "sierra" : "10.12",
            "high sierra" : "10.13",
            "mojave" : "10.14",
            "catalina" : "10.15",
            "big sur" : "10.16"
        }
        self.recovery_suffixes = (
            "RecoveryHDUpdate.pkg",
            "RecoveryHDMetaDmg.pkg"
        )
        self.min_macos = MIN_MACOS
        self.max_macos = MAX_MACOS
        self.macos_dict = []
    
    async def build_url(self, catalog_id):
        catalog = catalog_id.lower()
        version = self.max_macos
        url = "https://swscan.apple.com/content/catalogs/others/index-"
        url += "-".join([self.mac_os_names_url[str(x)] if str(x) in self.mac_os_names_url else "10."+str(x) for x in reversed(range(self.min_macos, version+1))])
        url += ".merged-1.sucatalog"
        ver_s = self.mac_os_names_url[str(version)] if str(version) in self.mac_os_names_url else "10."+str(version)
        if len(self.catalog_suffix[catalog]):
            url = url.replace(ver_s, ver_s+self.catalog_suffix[catalog]+"-"+ver_s)
        return url

    async def FetchCatalog(self, catalog_id = "publicseed"):
        url = await self.build_url(catalog_id)
        print (f"Fetching : {url}")
        self.raw_catalog = await self.HTTP.request(url, header=self.testagent)
        self.catalog_data = bytes(self.raw_catalog, "utf-8")
        return self.catalog_data

    async def ParseCatalog(self):
        root = plistlib.loads(self.catalog_data)
        products = root['Products']
        for product in products:
                if 'ExtendedMetaInfo' in products[product]:
                    IAMetaInfo = products[product]['ExtendedMetaInfo']
                    if 'InstallAssistantPackageIdentifiers' in IAMetaInfo:
                        IAPackageID = IAMetaInfo['InstallAssistantPackageIdentifiers']
                        if 'OSInstall' in IAPackageID:
                            if IAPackageID['OSInstall'] == 'com.apple.mpkg.OSInstall':
                                obj = macOS(product)
                                obj.packages = []
                                await self.GatherInformation(product, obj)
                                await self.AppendPackages(obj, product)
                                self.macos_dict.append(obj)
                        elif 'SharedSupport' in IAPackageID:
                            if IAPackageID["SharedSupport"].startswith("com.apple.pkg.InstallAssistant"):
                                obj = macOS(product)
                                obj.packages = []
                                await self.GatherInformation(product, obj)
                                await self.AppendPackages(obj, product)
                                self.macos_dict.append(obj)

    
    async def GatherInformation(self, product, object):
        root = plistlib.loads(self.catalog_data)
        target = root['Products'][product]
        try:
            resp = await self.HTTP.request(target['ServerMetadataURL'])
            smd = plistlib.loads(bytes(resp, "utf-8"))
            object.title = smd["localization"]["English"]["title"]
            object.version = smd["CFBundleShortVersionString"]
            dist_file = await self.HTTP.request(target['Distributions']['English'])
            build = version = name = "Unknown"
            build_search = "macOSProductBuildVersion" if "macOSProductBuildVersion" in dist_file else "BUILD"
            try:
                build = dist_file.split("<key>{}</key>".format(build_search))[1].split("<string>")[1].split("</string>")[0]
            except:
                pass
            object.build = build
        except KeyError:
            dist_file = await self.HTTP.request(target['Distributions']['English'])
            build = version = name = "Unknown"
            build_search = "macOSProductBuildVersion" if "macOSProductBuildVersion" in dist_file else "BUILD"
            vers_search  = "macOSProductVersion" if "macOSProductVersion" in dist_file else "VERSION"
            try:
                build = dist_file.split("<key>{}</key>".format(build_search))[1].split("<string>")[1].split("</string>")[0]
            except:
                pass
            try:
                version = dist_file.split("<key>{}</key>".format(vers_search))[1].split("<string>")[1].split("</string>")[0]
            except:
                pass
            try:
                name = re.search(r"<title>(.+?)</title>",dist_file).group(1)
            except:
                pass
            object.build = build
            object.title = name
            object.version = version

    async def AppendPackages(self, obj, product):
        print (f"Appending for {obj.title} - {product}")
        root = plistlib.loads(self.catalog_data)
        target = root['Products'][product]
        for package in target['Packages']:
            obj.packages.append((package['Size'], package['URL']))

