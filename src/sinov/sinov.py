import requests, lxml
from bs4 import BeautifulSoup

def get_all(mode, type, univer):
    url = "https://mandat.uzbmb.uz/Imtiyoz2024/GetAll"
    payload = {
        "Emode": mode,
        "Type": type,
        "UniverID": univer
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://mandat.uzbmb.uz",
        "Referer": "https://mandat.uzbmb.uz/Imtiyoz2024",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Cookie": ".AspNetCore.Antiforgery=UZ8z2jlaXdQ=CfDJ8JPr1NHW5mZOkqMsQpuRFMRZ87E43zUZUTIP24VZNoFXoMdNUkFrxzOBgwMuT5X1vbzo0LnIiOS3dO9sLuRa6eSFXdCvuhIHdU_NtBdu7338EMSUeTEbjcVsmM4Eafk33dNQPd0wB0T_8DTKh7OTx70"
    }
    response = requests.post(url, data=payload, headers=headers)
    # print(response.json())
    return response.json()


def get_mode(type):
    url = "https://mandat.uzbmb.uz/Imtiyoz2024/GetEmode"
    payload = {
        "Type": type
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://mandat.uzbmb.uz",
        "Referer": "https://mandat.uzbmb.uz/Imtiyoz2024",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Cookie": ".AspNetCore.Antiforgery=UZ8z2jlaXdQ=CfDJ8JPr1NHW5mZOkqMsQpuRFMRZ87E43zUZUTIP24VZNoFXoMdNUkFrxzOBgwMuT5X1vbzo0LnIiOS3dO9sLuRa6eSFXdCvuhIHdU_NtBdu7338EMSUeTEbjcVsmM4Eafk33dNQPd0wB0T_8DTKh7OTx70"
    }
    response = requests.post(url, data=payload, headers=headers)
    # print(response.json())
    return response.json()


def get_univer(mode, type):
    url = "https://mandat.uzbmb.uz/Imtiyoz2024/GetUniver"
    payload = {
        "Emode": mode,
        "Type": type
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://mandat.uzbmb.uz",
        "Referer": "https://mandat.uzbmb.uz/Imtiyoz2024",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Cookie": ".AspNetCore.Antiforgery=UZ8z2jlaXdQ=CfDJ8JPr1NHW5mZOkqMsQpuRFMRZ87E43zUZUTIP24VZNoFXoMdNUkFrxzOBgwMuT5X1vbzo0LnIiOS3dO9sLuRa6eSFXdCvuhIHdU_NtBdu7338EMSUeTEbjcVsmM4Eafk33dNQPd0wB0T_8DTKh7OTx70"
    }
    response = requests.post(url, data=payload, headers=headers)
    # print(response.json())
    return response.json()

res = requests.get("https://mandat.uzbmb.uz/Imtiyoz2024")
soup = BeautifulSoup(res.text, "lxml")
options = soup.find("div", class_="form-group").find_all("option")[1:]
for option in options:
    print(option.text)
    print(option['value'])
    type = option['value']
    mode = get_mode(type)[0]['value']
    print(mode)
    univer = get_univer(mode, type)[0]['value']
    print(univer)

    all = get_all(mode, type, univer)
    print(all)

    break