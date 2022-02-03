import fpdf
from fpdf import FPDF
from os import path

fpdf.set_global('FPDF_CACHE_MODE', 1)

# pdf document sizes
pdf_w = 216
pdf_h = 279

centeredImage = pdf_w / 2 - 1


class PDF(FPDF):
    def setImage(self, lang):
        if lang == 'ru':
            imagePath = path.abspath('alfabank_logo.png')
            self.image(imagePath, centeredImage, 34, 33.3, 9.4)
        else:
            imagePath = path.abspath('alfabank_logo_eng.png')
            self.image(imagePath, centeredImage, 34, 6, 9.4)
        self.cell(w=50, align='C', border=0)

    def setTitle(self, data):
        self.set_xy(24.4, 67.8)
        self.set_font('Bold', '', 16.8)
        self.set_text_color(0, 0, 0)
        self.cell(w=160, align='L', ln=1, txt=data['status_ru'], border=0)

        # organization
        self.set_xy(24.4, 78.3)
        self.set_font('Regular', '', 13.4)
        self.cell(w=80, align='L', txt='Организация', border=0)

        self.set_xy(110.4, 78.3)
        self.cell(w=80, align='L', txt=data['organization'], border=0)

        # date_of_payment
        self.set_xy(24.4, 86.8)
        self.cell(w=80, align='L', txt='Дата оплаты', border=0)

        self.set_xy(110.4, 86.8)
        self.cell(w=80, align='L', txt=data['date_of_payment'], border=0)

        # order_number
        self.set_xy(24.4, 95)
        self.cell(w=80, align='L', txt='Номер заказа', border=0)

        self.set_xy(110.4, 95)
        self.cell(w=80, align='L', txt=data['order_number'], border=0)

        # amount_of_payment
        self.set_xy(24.4, 103.4)
        self.cell(w=80, align='L', txt='Сумма платежа', border=0)

        self.set_xy(110.4, 103.4)
        self.cell(w=80, align='L', txt=data['amount_of_payment'], border=0)

        # payment_commission
        self.set_xy(24.4, 111.6)
        self.cell(w=80, align='L', txt='Комиссия за платеж', border=0)

        self.set_xy(110.4, 111.6)
        self.cell(w=80, align='L', txt=data['payment_commission'], border=0)

        # card_number
        self.set_xy(24.4, 124)
        self.cell(w=80, align='L', txt='Номер карты', border=0)

        self.set_xy(110.4, 124)
        self.cell(w=80, align='L', txt=data['card_number'], border=0)

        # name
        self.set_xy(24.4, 132.4)
        self.cell(w=80, align='L', txt='Имя владельца', border=0)

        self.set_xy(110.4, 132.4)
        self.cell(w=80, align='L', txt=data['name'], border=0)

        # terminal_id
        self.set_xy(24.4, 140.6)
        self.cell(w=80, align='L', txt='Терминал ID', border=0)

        self.set_xy(110.4, 140.6)
        self.cell(w=80, align='L', txt=data['terminal_id'], border=0)

        # refnum
        self.set_xy(24.4, 149.1)
        self.cell(w=80, align='L', txt='Refnum', border=0)

        self.set_xy(110.4, 149.1)
        self.cell(w=80, align='L', txt=data['refnum'], border=0)

        # auth_code
        self.set_xy(24.4, 157.3)
        self.cell(w=80, align='L', txt='Код авторизации', border=0)

        self.set_xy(110.4, 157.3)
        self.cell(w=80, align='L', txt=data['auth_code'], border=0)

        if data['rejection']:
            self.set_xy(14, 178)
            self.set_font('Regular', '', 12)
            # self.cell(w=170, align='L', ln=1, txt=data['rejection'], border=0)
            self.multi_cell(w=170, h=6, align='L', txt=data['rejection'], border=0)

    def setEngTitle(self, data):
        self.set_xy(24.4, 67.8)
        self.set_font('Bold', '', 16.8)
        self.set_text_color(0, 0, 0)
        self.cell(w=160, align='L', ln=1, txt=data['status_en'], border=0)

        # organization
        self.set_xy(24.4, 78.3)
        self.set_font('Regular', '', 13.4)
        self.cell(w=80, align='L', txt='Organization', border=0)

        self.set_xy(110.4, 78.3)
        self.cell(w=80, align='L', txt=data['organization'], border=0)

        # date_of_payment
        self.set_xy(24.4, 86.8)
        self.cell(w=80, align='L', txt='Date', border=0)

        self.set_xy(110.4, 86.8)
        self.cell(w=80, align='L', txt=data['date_of_payment'], border=0)

        # order_number
        self.set_xy(24.4, 95)
        self.cell(w=80, align='L', txt='Order number', border=0)

        self.set_xy(110.4, 95)
        self.cell(w=80, align='L', txt=data['order_number'], border=0)

        # amount_of_payment
        self.set_xy(24.4, 103.4)
        self.cell(w=80, align='L', txt='Payment amount', border=0)

        self.set_xy(110.4, 103.4)
        self.cell(w=80, align='L', txt=data['amount_of_payment'], border=0)

        # payment_commission
        self.set_xy(24.4, 111.6)
        self.cell(w=80, align='L', txt='Payment fee', border=0)

        self.set_xy(110.4, 111.6)
        self.cell(w=80, align='L', txt=data['payment_commission'], border=0)

        # card_number
        self.set_xy(24.4, 124)
        self.cell(w=80, align='L', txt='Card number', border=0)

        self.set_xy(110.4, 124)
        self.cell(w=80, align='L', txt=data['card_number'], border=0)

        # name
        self.set_xy(24.4, 132.4)
        self.cell(w=80, align='L', txt='Cardholder name', border=0)

        self.set_xy(110.4, 132.4)
        self.cell(w=80, align='L', txt=data['name'], border=0)

        # terminal_id
        self.set_xy(24.4, 140.6)
        self.cell(w=80, align='L', txt='Terminal ID', border=0)

        self.set_xy(110.4, 140.6)
        self.cell(w=80, align='L', txt=data['terminal_id'], border=0)

        # refnum
        self.set_xy(24.4, 149.1)
        self.cell(w=80, align='L', txt='Refnum', border=0)

        self.set_xy(110.4, 149.1)
        self.cell(w=80, align='L', txt=data['refnum'], border=0)

        # auth_code
        self.set_xy(24.4, 157.3)
        self.cell(w=80, align='L', txt='Authorization code', border=0)

        self.set_xy(110.4, 157.3)
        self.cell(w=80, align='L', txt=data['auth_code'], border=0)

        if data['rejection']:
            self.set_xy(14, 178)
            self.set_font('Regular', '', 12)
            self.multi_cell(w=170, h=6, align='L', txt=data['rejection'], border=0)


def create_pdf_cheque(data, language):
    # path to image
    # imagePath = '/usr/lib/python2.7/dist-packages/ego_auth/lib/cheque_pdf/alfabank_logo.png'
    # path to font
    # fontPathRobotoRegular ='/usr/lib/python2.7/dist-packages/ego_auth/lib/cheque_pdf/Roboto-Regular.ttf'
    # fontPathRobotoBold = '/usr/lib/python2.7/dist-packages/ego_auth/lib/cheque_pdf/Roboto-Bold.ttf'
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
    if language == 'en':
        pdf.setEngTitle(data)
        pdf.setImage('en')
    else:
        pdf.setTitle(data)
        pdf.setImage('ru')
    # set image on page
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
