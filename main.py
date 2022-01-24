from fpdf import FPDF
from os import path

# path to image
imagePath = path.abspath('alfabank_logo.png')
# path to font
fontPathRobotoRegular = path.abspath('Roboto-Regular.ttf')
fontPathRobotoBold = path.abspath('Roboto-Bold.ttf')
# pdf document sizes
pdf_w = 210
pdf_h = 297

centeredImage = pdf_w / 2 - 20

dataDict = {
    'organization': 'ips_test',
    'date_of_payment': '123',
    'order_number': '123efcsd',
    'amount_of_payment': '123.00 RUB',
    'payment_commission': '0 RUB',
    'card_number': '2137 **** **** 1234',
    'name': 'YY',
    'terminal_id': 'akjsdnasd',
    'refnum': '6758617982031',
    'auth_code': '200'
}

class PDF(FPDF):
    def setImage(self):
        self.image(imagePath, centeredImage, 40, 35)
        self.cell(w=180, align='C', border=0)

    def setTitle(self):
        self.set_xy(20, 75)
        self.set_font('Roboto-Bold', '', 16)
        self.set_text_color(11, 31, 53)
        self.cell(w=160, align='L', ln=1, txt='Оплата отклонена', border=0)

        # organization
        self.set_xy(20, 90)
        self.set_font('Roboto-Regular', '', 12)
        self.cell(w=80, align='L', txt='Организация', border=0)

        self.set_xy(100, 90)
        self.cell(w=80, align='L', txt=dataDict['organization'], border=0)

        # date_of_payment
        self.set_xy(20, 100)
        self.cell(w=80, align='L', txt='Дата оплаты', border=0)

        self.set_xy(100, 100)
        self.cell(w=80, align='L', txt=dataDict['date_of_payment'], border=0)

        # order_number
        self.set_xy(20, 110)
        self.cell(w=80, align='L', txt='Номер заказа', border=0)

        self.set_xy(100, 110)
        self.cell(w=80, align='L', txt=dataDict['order_number'], border=0)

        # amount_of_payment
        self.set_xy(20, 120)
        self.cell(w=80, align='L', txt='Сумма платежа', border=0)

        self.set_xy(100, 120)
        self.cell(w=80, align='L', txt=dataDict['amount_of_payment'], border=0)

        # payment_commission
        self.set_xy(20, 130)
        self.cell(w=80, align='L', txt='Комиссия за платеж', border=0)

        self.set_xy(100, 130)
        self.cell(w=80, align='L', txt=dataDict['payment_commission'], border=0)

        # card_number
        self.set_xy(20, 145)
        self.cell(w=80, align='L', txt='Номер карты', border=0)

        self.set_xy(100, 145)
        self.cell(w=80, align='L', txt=dataDict['card_number'], border=0)

        # name
        self.set_xy(20, 155)
        self.cell(w=80, align='L', txt='Имя владельца', border=0)

        self.set_xy(100, 155)
        self.cell(w=80, align='L', txt=dataDict['name'], border=0)

        # terminal_id
        self.set_xy(20, 165)
        self.cell(w=80, align='L', txt='Терминал ID', border=0)

        self.set_xy(100, 165)
        self.cell(w=80, align='L', txt=dataDict['terminal_id'], border=0)

        # refnum
        self.set_xy(20, 175)
        self.cell(w=80, align='L', txt='Refnum', border=0)

        self.set_xy(100, 175)
        self.cell(w=80, align='L', txt=dataDict['refnum'], border=0)

        # auth_code
        self.set_xy(20, 185)
        self.cell(w=80, align='L', txt='Код авторизации', border=0)

        self.set_xy(100, 185)
        self.cell(w=80, align='L', txt=dataDict['auth_code'], border=0)

        self.set_xy(15, 210)
        self.set_font('Roboto-Bold', '', 12)
        self.cell(w=160, align='L', ln=1, txt='Причина отклонения', border=0)

        self.set_xy(15, 218)
        self.set_font('Roboto-Regular', '', 10)
        self.cell(w=120, align='L', ln=1,
                  txt='Операция отклонена. Проверьте введенные данные, '
                      'достаточность средств на счете и повторите операцию', border=0)


# generate class
pdf = PDF()
# add Roboto font
pdf.add_font('Roboto-Regular', '', fontPathRobotoRegular, uni=True)
pdf.add_font('Roboto-Bold', '', fontPathRobotoBold, uni=True)
# create page
pdf.add_page()
# set title on page
pdf.setTitle()
# set image on page
pdf.setImage()
# generate pdf document
pdf.output('test.pdf')
