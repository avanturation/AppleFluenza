import discord
import orjson
from utils.parser import Parser
from hurry.filesize import size, alternative

idevice_name = {
    "i386" : "iPhone Simulator",
    "x86_64" : "iPhone Simulator",
    "iPhone1,1" : "iPhone",
    "iPhone1,2" : "iPhone 3G",
    "iPhone2,1" : "iPhone 3GS",
    "iPhone3,1" : "iPhone 4",
    "iPhone3,2" : "iPhone 4 GSM Rev A",
    "iPhone3,3" : "iPhone 4 CDMA",
    "iPhone4,1" : "iPhone 4S",
    "iPhone5,1" : "iPhone 5 (GSM)",
    "iPhone5,2" : "iPhone 5 (GSM+CDMA)",
    "iPhone5,3" : "iPhone 5C (GSM)",
    "iPhone5,4" : "iPhone 5C (Global)",
    "iPhone6,1" : "iPhone 5S (GSM)",
    "iPhone6,2" : "iPhone 5S (Global)",
    "iPhone7,1" : "iPhone 6 Plus",
    "iPhone7,2" : "iPhone 6",
    "iPhone8,1" : "iPhone 6s",
    "iPhone8,2" : "iPhone 6s Plus",
    "iPhone8,4" : "iPhone SE (GSM)",
    "iPhone9,1" : "iPhone 7",
    "iPhone9,2" : "iPhone 7 Plus",
    "iPhone9,3" : "iPhone 7",
    "iPhone9,4" : "iPhone 7 Plus",
    "iPhone10,1" : "iPhone 8",
    "iPhone10,2" : "iPhone 8 Plus",
    "iPhone10,3" : "iPhone X Global",
    "iPhone10,4" : "iPhone 8",
    "iPhone10,5" : "iPhone 8 Plus",
    "iPhone10,6" : "iPhone X GSM",
    "iPhone11,2" : "iPhone XS",
    "iPhone11,4" : "iPhone XS Max",
    "iPhone11,6" : "iPhone XS Max Global",
    "iPhone11,8" : "iPhone XR",
    "iPhone12,1" : "iPhone 11",
    "iPhone12,3" : "iPhone 11 Pro",
    "iPhone12,5" : "iPhone 11 Pro Max",
    "iPhone12,8" : "iPhone SE 2nd Gen",
    "iPod1,1" : "1st Gen iPod",
    "iPod2,1" : "2nd Gen iPod",
    "iPod3,1" : "3rd Gen iPod",
    "iPod4,1" : "4th Gen iPod",
    "iPod5,1" : "5th Gen iPod",
    "iPod7,1" : "6th Gen iPod",
    "iPod9,1" : "7th Gen iPod",
    "iPad1,1" : "iPad",
    "iPad1,2" : "iPad 3G",
    "iPad2,1" : "2nd Gen iPad",
    "iPad2,2" : "2nd Gen iPad GSM",
    "iPad2,3" : "2nd Gen iPad CDMA",
    "iPad2,4" : "2nd Gen iPad New Revision",
    "iPad3,1" : "3rd Gen iPad",
    "iPad3,2" : "3rd Gen iPad CDMA",
    "iPad3,3" : "3rd Gen iPad GSM",
    "iPad2,5" : "iPad mini",
    "iPad2,6" : "iPad mini GSM+LTE",
    "iPad2,7" : "iPad mini CDMA+LTE",
    "iPad3,4" : "4th Gen iPad",
    "iPad3,5" : "4th Gen iPad GSM+LTE",
    "iPad3,6" : "4th Gen iPad CDMA+LTE",
    "iPad4,1" : "iPad Air (WiFi)",
    "iPad4,2" : "iPad Air (GSM+CDMA)",
    "iPad4,3" : "1st Gen iPad Air (China)",
    "iPad4,4" : "iPad mini Retina (WiFi)",
    "iPad4,5" : "iPad mini Retina (GSM+CDMA)",
    "iPad4,6" : "iPad mini Retina (China)",
    "iPad4,7" : "iPad mini 3 (WiFi)",
    "iPad4,8" : "iPad mini 3 (GSM+CDMA)",
    "iPad4,9" : "iPad Mini 3 (China)",
    "iPad5,1" : "iPad mini 4 (WiFi)",
    "iPad5,2" : "4th Gen iPad mini (WiFi+Cellular)",
    "iPad5,3" : "iPad Air 2 (WiFi)",
    "iPad5,4" : "iPad Air 2 (Cellular)",
    "iPad6,3" : "iPad Pro (9.7 inch, WiFi)",
    "iPad6,4" : "iPad Pro (9.7 inch, WiFi+LTE)",
    "iPad6,7" : "iPad Pro (12.9 inch, WiFi)",
    "iPad6,8" : "iPad Pro (12.9 inch, WiFi+LTE)",
    "iPad6,11" : "iPad (2017)",
    "iPad6,12" : "iPad (2017)",
    "iPad7,1" : "iPad Pro 2nd Gen (WiFi)",
    "iPad7,2" : "iPad Pro 2nd Gen (WiFi+Cellular)",
    "iPad7,3" : "iPad Pro 10.5-inch",
    "iPad7,4" : "iPad Pro 10.5-inch",
    "iPad7,5" : "iPad 6th Gen (WiFi)",
    "iPad7,6" : "iPad 6th Gen (WiFi+Cellular)",
    "iPad7,11" : "iPad 7th Gen 10.2-inch (WiFi)",
    "iPad7,12" : "iPad 7th Gen 10.2-inch (WiFi+Cellular)",
    "iPad8,1" : "iPad Pro 11 inch (WiFi)",
    "iPad8,2" : "iPad Pro 11 inch (1TB, WiFi)",
    "iPad8,3" : "iPad Pro 11 inch (WiFi+Cellular)",
    "iPad8,4" : "iPad Pro 11 inch (1TB, WiFi+Cellular)",
    "iPad8,5" : "iPad Pro 12.9 inch 3rd Gen (WiFi)",
    "iPad8,6" : "iPad Pro 12.9 inch 3rd Gen (1TB, WiFi)",
    "iPad8,7" : "iPad Pro 12.9 inch 3rd Gen (WiFi+Cellular)",
    "iPad8,8" : "iPad Pro 12.9 inch 3rd Gen (1TB, WiFi+Cellular)",
    "iPad8,9" : "iPad Pro 11 inch 2nd Gen (WiFi)",
    "iPad8,10" : "iPad Pro 11 inch 2nd Gen (WiFi+Cellular)",
    "iPad8,11" : "iPad Pro 12.9 inch 4th Gen (WiFi)",
    "iPad8,12" : "iPad Pro 12.9 inch 4th Gen (WiFi+Cellular)",
    "iPad11,1" : "iPad mini 5th Gen (WiFi)",
    "iPad11,2" : "iPad mini 5th Gen",
    "iPad11,3" : "iPad Air 3rd Gen (WiFi)",
    "iPad11,4" : "iPad Air 3rd Gen"
}

async def ipsw_info (device_id):
    HTTP = Parser()
    json = await HTTP.request(f"https://api.ipsw.me/v2/{device_id}/latest/info.json")
    json = orjson.loads(json)
    json = json[0]
    embed = discord.Embed (
        title = f"{idevice_name[device_id]} 정보"
    )
    embed.add_field (
        name = "iOS 버전",
        value = f"iOS {json['version']}",
        inline = True
    )
    embed.add_field (
        name = "빌드 ID",
        value = json["buildid"],
        inline = True
    )
    embed.add_field (
        name = "파일 용량",
        value = size(int(json["filesize"]), system = alternative),
        inline = True
    )
    embed.add_field (
        name = "릴리즈 날짜",
        value = json["datefound"][:10],
        inline = True
    )
    embed.add_field (
        name = "다운로드",
        value = f"[클릭]({json['url']})",
        inline = False
    )
    embed.add_field (
        name = "MD5 체크섬",
        value = json['md5sum'],
        inline = True
    )
    return embed