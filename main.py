import fpdf
from fpdf import FPDF
from os import path

fpdf.set_global('FPDF_CACHE_MODE', 1)

labels_by_language = {
    "ru": {
        "fail_header": "Оплата отклонена",
        "success_header": "Платёж успешно завершён",
        "organization": "Организация",
        "date": "Дата оплаты",
        "order_number": "Номер заказа",
        "amount": "Сумма платежа",
        "commission": "Комиссия за платеж",
        "cardnumber": "Номер карты",
        "cardholder": "Имя владельца",
        "terminal": "Терминал ID",
        "refnum": "Refnum",
        "auth_code": "Код авторизации",
        "fail_reasone": "Причина отклонения"
    },
    "en":{
        "fail_header": "Payment declined",
        "success_header": "Payment completed successfully",
        "organization": "Organisation",
        "date": "Date",
        "order_number": "Order number",
        "amount": "Payment amount",
        "commission": "Payment fee",
        "cardnumber": "Card number",
        "cardholder": "Cardholder name",
        "terminal": "Terminal ID",
        "refnum": "Refnum",
        "auth_code": "Authorization code",
        "fail_reasone": "Reason for rejection"
    },
    "ua":{
        "organization": "Організація",
        "date": "Дата",
        "order_number": "Номер замовлення",
        "amount": "Сума платежу",
        "commission": "Комісія за платіж",
        "cardnumber": "Номер картки",
        "cardholder": "Власник картки",
        "terminal": "Термінал ID",
        "refnum": "Refnum",
        "auth_code": "Код авторизації",
    },
    "fr":{
        "organization": "Organisation",
        "date": "Date",
        "order_number": "Numéro de la commande",
        "amount": "Montant",
        "commission": "Commission",
        "cardnumber": "Numéro de la carte",
        "cardholder": "Le nom du détenteur",
        "terminal": "Terminal ID",
        "refnum": "Refnum",
        "auth_code": "Code d’autorisation",
    },
    "es":{
        "organization": "Organizacion",
        "date": "Fecha",
        "order_number": "Número del pedido",
        "amount": "Suma a paga",
        "commission": "Comisión por pago",
        "cardnumber": "Número de la tarjeta",
        "cardholder": "Tenedor de la tarjeta",
        "terminal": "Terminal ID",
        "refnum": "Refnum",
        "auth_code": "Código de la autorización",
    },
    "kz":{
        "organization": "Ұйым",
        "date": "Күні",
        "order_number": "Тапсырыстың нөмірі",
        "amount": "Төлем сомасы",
        "commission": "Төлем комиссиясы",
        "cardnumber": "Card number",
        "cardholder": "Иесінің аты",
        "terminal": "Terminal ID",
        "refnum": "Refnum",
        "auth_code": "Approval code",
    },
    "it":{
        "organization": "Organizzazione",
        "date": "Data",
        "order_number": "Numero dell'ordine",
        "amount": "Importo del pagamento",
        "commission": "Commissione per il pagamento",
        "cardnumber": "Card number",
        "cardholder": "Nome del titolare",
        "terminal": "Terminal ID",
        "refnum": "Refnum",
        "auth_code": "Approval code",
    },
    "de":{
        "organization": "Organisation",
        "date": "Datum",
        "order_number": "Auftragsnummer",
        "amount": "Zahlungsbetrag",
        "commission": "Zahlungsprovision",
        "cardnumber": "Kartennummer",
        "cardholder": "Karteninhaber",
        "terminal": "Terminal ID ",
        "refnum": "Refnum",
        "auth_code": "Autorisierungscode",
    },
    "zn":{
        "organization": "Organizzazione",
        "date": "Data",
        "terminal": "ID",
        "refnum": "Refnum",
    }
}

coordinates_by_language = {
    "main": {
        "header": 67.8,
        "organization": 78.3,
        "date": 86.8,
        "order_number": 95,
        "amount": 103.4,
        "commission": 111.6,
        "cardnumber": 124,
        "cardholder": 132.4,
        "terminal": 140.6,
        "refnum": 149.1,
        "auth_code": 157.3,
        "reasone_title": 184,
        "fail_reasone": 194.2,
    },
    "another": {
        "header": 0,
        "organization": 67.2,
        "date": 75.4,
        "order_number": 83.8,
        "amount": 92,
        "commission": 100.6,
        "cardnumber": 113,
        "cardholder": 121.2,
        "terminal": 129.6,
        "refnum": 137.8,
        "auth_code": 146.4,
        "fail_reasone": 172.5
    }
}

# pdf document sizes
pdf_w = 216
pdf_h = 279

centeredImage = pdf_w / 2 - 1

class PDF(FPDF):
    def setImage(self, lang):
        if lang == 'ru':
            # path to image
            imagePath = path.abspath('alfabank_logo.png')
            # imagePath = '/usr/lib/python2.7/dist-packages/ego_auth/lib/cheque_pdf/alfabank_logo.png'
            self.image(imagePath, centeredImage, 34, 33.3, 9.4)
        else:
            # path to image
            # imagePath = '/usr/lib/python2.7/dist-packages/ego_auth/lib/cheque_pdf/alfabank_logo_eng.png'
            imagePath = path.abspath('alfabank_logo_eng.png')
            self.image(imagePath, centeredImage, 34, 6, 9.4)
        self.cell(w=50, align='C', border=0)

    def setTitle(self, labels, cords, data):
        self.set_xy(24.4, cords.get("header", ""))
        self.set_font('Bold', '', 16.8)
        self.set_text_color(0, 0, 0)
        self.cell(w=160, align='L', ln=1, txt=labels.get("header", ""), border=0)

        # organization
        self.set_xy(24.4, cords.get("organization", ""))
        self.set_font('Regular', '', 13.4)
        self.cell(w=80, align='L', txt=labels.get("organization", ""), border=0)

        self.set_xy(110.4, cords.get("organization", ""))
        self.cell(w=80, align='L', txt=data['organization'], border=0)

        # date_of_payment
        self.set_xy(24.4, cords.get("date", ""))
        self.cell(w=80, align='L', txt=labels.get("date", ""), border=0)

        self.set_xy(110.4, cords.get("date", ""))
        self.cell(w=80, align='L', txt=data['date_of_payment'], border=0)

        # order_number
        self.set_xy(24.4, cords.get("order_number", ""))
        self.cell(w=80, align='L', txt=labels.get("order_number", ""), border=0)

        self.set_xy(110.4, cords.get("order_number", ""))
        self.cell(w=80, align='L', txt=data['order_number'], border=0)

        # amount_of_payment
        self.set_xy(24.4, cords.get("amount", ""))
        self.cell(w=80, align='L', txt=labels.get("amount", ""), border=0)

        self.set_xy(110.4, cords.get("amount", ""))
        self.cell(w=80, align='L', txt=data['amount_of_payment'], border=0)

        # payment_commission
        self.set_xy(24.4, cords.get("commission", ""))
        self.cell(w=80, align='L', txt=labels.get("commission", ""), border=0)

        self.set_xy(110.4, cords.get("commission", ""))
        self.cell(w=80, align='L', txt=data['payment_commission'], border=0)

        # card_number
        self.set_xy(24.4, cords.get("cardnumber", ""))
        self.cell(w=80, align='L', txt=labels.get("cardnumber", ""), border=0)

        self.set_xy(110.4, cords.get("cardnumber", ""))
        self.cell(w=80, align='L', txt=data['card_number'], border=0)

        # name
        self.set_xy(24.4, cords.get("cardholder", ""))
        self.cell(w=80, align='L', txt=labels.get("cardholder", ""), border=0)

        self.set_xy(110.4, cords.get("cardholder", ""))
        self.cell(w=80, align='L', txt=data['name'], border=0)

        # terminal_id
        self.set_xy(24.4, cords.get("terminal", ""))
        self.cell(w=80, align='L', txt=labels.get("terminal", ""), border=0)

        self.set_xy(110.4, cords.get("terminal", ""))
        self.cell(w=80, align='L', txt=data['terminal_id'], border=0)

        # refnum
        self.set_xy(24.4, cords.get("refnum", ""))
        self.cell(w=80, align='L', txt=labels.get("refnum", ""), border=0)

        self.set_xy(110.4, cords.get("refnum", ""))
        self.cell(w=80, align='L', txt=data['refnum'], border=0)

        # auth_code
        self.set_xy(24.4, cords.get("auth_code", ""))
        self.cell(w=80, align='L', txt=labels.get("auth_code", ""), border=0)

        self.set_xy(110.4, cords.get("auth_code", ""))
        self.cell(w=80, align='L', txt=data['auth_code'], border=0)

        if data['rejection']:

            if labels.get('fail_reasone'):
                self.set_xy(13.8, cords.get("reasone_title", ""))
                self.set_font('Bold', '', 14)
                self.multi_cell(w=170, h=6, align='L', txt=labels.get('fail_reasone', ''), border=0)

            self.set_xy(13.8, cords.get("fail_reasone", ""))
            self.set_font('Regular', '', 12)
            self.multi_cell(w=170, h=6, align='L', txt=data['rejection'], border=0)


def create_pdf_cheque(data, language):
    labels = labels_by_language[language]

    if data['success']:
        labels["header"] = labels.get("success_header", "")
    else:
        labels["header"] = labels.get("fail_header", "")

    if language == 'ru' or language == 'en':
        lang_for_cords = 'main'
    else:
        lang_for_cords = 'another'
    cords = coordinates_by_language[lang_for_cords]

    # path to font
    # fontPathRegular = '/usr/lib/python2.7/dist-packages/ego_auth/lib/cheque_pdf/Arial-Regular.ttf'
    # fontPathBold = '/usr/lib/python2.7/dist-packages/ego_auth/lib/cheque_pdf/Arial-Bold.ttf'
    fontPathRegular = path.abspath('Arial-Regular.ttf')
    fontPathBold = path.abspath('Arial-Bold.ttf')
    # generate class
    pdf = PDF('P', 'mm', [216, 279])
    # add Roboto font
    pdf.add_font('Regular', '', fontPathRegular, uni=True)
    pdf.add_font('Bold', '', fontPathBold, uni=True)
    # create page
    pdf.add_page()
    # set title on page

    pdf.setTitle(labels, cords, data)
    # set image on page
    pdf.setImage(language)
    # generate pdf document
    # return pdf.output(dest='S')
    return pdf.output('test.pdf')

dataDict = {
    'status_ru': "Платёж успешно завершён",
    'status_en': "Payment completed successfully",
    'organization': "test shop",
    'date_of_payment': "22.22.2222",
    'order_number': '123',
    'amount_of_payment': '1234',
    'payment_commission': '0 RUB',
    'card_number': '1231231231312',
    'name': 'ASD ADS',
    'terminal_id': '',
    'refnum': '',
    'auth_code': '',
    'success': True,
    'rejection': 'Операция отклонена. Проверьте введенные данные, достаточность средств на счёте и повторите операцию.'
}

create_pdf_cheque(dataDict, 'ru')
