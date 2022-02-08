import fpdf
from fpdf import FPDF
from os import path


fpdf.set_global('FPDF_CACHE_MODE', 1)
reasonMap = {
    'ru': {
        '3dsecure/reject': "Операция невозможна. Аутентификация держателя карты завершена неуспешно.",
        '3dsecure/failed': "Операция невозможна. Аутентификация держателя карты завершена неуспешно.",
        '3dsecure/timeout': "Операция невозможна. Аутентификация держателя карты завершена неуспешно.",
        '3dsecure/network': "Операция невозможна. Аутентификация держателя карты завершена неуспешно.",
        'system/ok': "",
        'bank/common': "Операция отклонена. Проверьте введенные данные, достаточность средств на счёте и повторите операцию.",
        'bank/fraud': "Операция отклонена. Проверьте введенные данные, достаточность средств на счёте и повторите операцию.",
        'bank/network': "Операция отклонена. Проверьте введенные данные, достаточность средств на счёте и повторите операцию.",
        'bank/funds': "Операция отклонена. Проверьте введенные данные, достаточность средств на счёте и повторите операцию.",
        'bank/account': "Операция отклонена. Проверьте введенные данные, достаточность средств на счёте и повторите операцию.",
        'bank/limit': "Операция отклонена. Проверьте введенные данные, достаточность средств на счёте и повторите операцию.",
        'bank/timeout': "Операция отклонена. Проверьте введенные данные, достаточность средств на счёте и повторите операцию.",
        'system/black-list': "Операция отклонена. Проверьте введенные данные, достаточность средств на счёте и повторите операцию.",
        'system/max_attempts': "Операция отклонена. Проверьте введенные данные, достаточность средств на счёте и повторите операцию.",
        'system/in_progress': "",
        'system/network': "Операция отклонена. Проверьте введенные данные, достаточность средств на счёте и повторите операцию.",
        'system/fraud': "Операция отклонена. Проверьте введенные данные, достаточность средств на счёте и повторите операцию.",
        'system/unavailable_method': "Операция отклонена. Проверьте введенные данные, достаточность средств на счёте и повторите операцию.",
        'system/operator': "Операция отклонена. Проверьте введенные данные, достаточность средств на счёте и повторите операцию.",
        'system/common': "Операция отклонена. Проверьте введенные данные, достаточность средств на счёте и повторите операцию.",
        'system/timeout': "Операция отклонена. Проверьте введенные данные, достаточность средств на счёте и повторите операцию.",
        'system/session': "Операция отклонена. Проверьте введенные данные, достаточность средств на счёте и повторите операцию.",
        'system/denied': "Операция отклонена. Проверьте введенные данные, достаточность средств на счёте и повторите операцию.",
        'system/already_processed': "Операция отклонена. Проверьте введенные данные, достаточность средств на счёте и повторите операцию.",
        'system/cancel_denied': "Операция отклонена. Проверьте введенные данные, достаточность средств на счёте и повторите операцию.",
        'user/timeout': "Операция отклонена. Проверьте введенные данные, достаточность средств на счёте и повторите операцию.",
        'user/cancel': "Операция отклонена. Проверьте введенные данные, достаточность средств на счёте и повторите операцию.",
        'user/duplicate': "Операция отклонена. Проверьте введенные данные, достаточность средств на счёте и повторите операцию.",
        'user/network': "Операция отклонена. Проверьте введенные данные, достаточность средств на счёте и повторите операцию.",
        'user/card_not_binded': "Операция отклонена. Проверьте введенные данные, достаточность средств на счёте и повторите операцию.",
        'user/unsupported_card': "Операция отклонена. Проверьте введенные данные, достаточность средств на счёте и повторите операцию.",
        'user/interaction_timeout': "Операция отклонена. Проверьте введенные данные, достаточность средств на счёте и повторите операцию.",
        'default': "Операция отклонена. Проверьте введенные данные, достаточность средств на счёте и повторите операцию.",
    },
    'en': {
        '3dsecure/reject': "Operation is not possible. Cardholder authentication failed.",
        '3dsecure/failed': "Operation is not possible. Cardholder authentication failed.",
        '3dsecure/timeout': "Operation is not possible. Cardholder authentication failed.",
        '3dsecure/network': "Operation is not possible. Cardholder authentication failed.",
        'system/ok': "",
        'bank/common': "Operation rejected. Check the entered data, the sufficiency of funds on the account and repeat the operation.",
        'bank/fraud': "Operation rejected. Check the entered data, the sufficiency of funds on the account and repeat the operation.",
        'bank/network': "Operation rejected. Check the entered data, the sufficiency of funds on the account and repeat the operation.",
        'bank/funds': "Operation rejected. Check the entered data, the sufficiency of funds on the account and repeat the operation.",
        'bank/account': "Operation rejected. Check the entered data, the sufficiency of funds on the account and repeat the operation.",
        'bank/limit': "Operation rejected. Check the entered data, the sufficiency of funds on the account and repeat the operation.",
        'bank/timeout': "Operation rejected. Check the entered data, the sufficiency of funds on the account and repeat the operation.",
        'system/black-list': "Operation rejected. Check the entered data, the sufficiency of funds on the account and repeat the operation.",
        'system/max_attempts': "Operation rejected. Check the entered data, the sufficiency of funds on the account and repeat the operation.",
        'system/in_progress': "",
        'system/network': "Operation rejected. Check the entered data, the sufficiency of funds on the account and repeat the operation.",
        'system/fraud': "Operation rejected. Check the entered data, the sufficiency of funds on the account and repeat the operation.",
        'system/unavailable_method': "Operation rejected. Check the entered data, the sufficiency of funds on the account and repeat the operation.",
        'system/operator': "Operation rejected. Check the entered data, the sufficiency of funds on the account and repeat the operation.",
        'system/common': "Operation rejected. Check the entered data, the sufficiency of funds on the account and repeat the operation.",
        'system/timeout': "Operation rejected. Check the entered data, the sufficiency of funds on the account and repeat the operation.",
        'system/session': "Operation rejected. Check the entered data, the sufficiency of funds on the account and repeat the operation.",
        'system/denied': "Operation rejected. Check the entered data, the sufficiency of funds on the account and repeat the operation.",
        'system/already_processed': "Operation rejected. Check the entered data, the sufficiency of funds on the account and repeat the operation.",
        'system/cancel_denied': "Operation rejected. Check the entered data, the sufficiency of funds on the account and repeat the operation.",
        'user/timeout': "Operation rejected. Check the entered data, the sufficiency of funds on the account and repeat the operation.",
        'user/cancel': "Operation rejected. Check the entered data, the sufficiency of funds on the account and repeat the operation.",
        'user/duplicate': "Operation rejected. Check the entered data, the sufficiency of funds on the account and repeat the operation.",
        'user/network': "Operation rejected. Check the entered data, the sufficiency of funds on the account and repeat the operation.",
        'user/card_not_binded': "Operation rejected. Check the entered data, the sufficiency of funds on the account and repeat the operation.",
        'user/unsupported_card': "Operation rejected. Check the entered data, the sufficiency of funds on the account and repeat the operation.",
        'user/interaction_timeout': "Operation rejected. Check the entered data, the sufficiency of funds on the account and repeat the operation.",
        'default': "Operation rejected. Check the entered data, the sufficiency of funds on the account and repeat the operation.",
    },
    'ua': {
        '3dsecure/reject': "Операція неможлива. Аутентифікація власника картки завершена неуспішно.",
        '3dsecure/failed': "Операція неможлива. Аутентифікація власника картки завершена неуспішно.",
        '3dsecure/timeout': "Операція неможлива. Аутентифікація власника картки завершена неуспішно.",
        '3dsecure/network': "Операція неможлива. Аутентифікація власника картки завершена неуспішно.",
        'system/ok': "",
        'bank/common': "Операцію відхилено. Перевірте введені дані, достатність коштів на рахунку та повторіть операцію.",
        'bank/fraud': "Операцію відхилено. Перевірте введені дані, достатність коштів на рахунку та повторіть операцію.",
        'bank/network': "Операцію відхилено. Перевірте введені дані, достатність коштів на рахунку та повторіть операцію.",
        'bank/funds': "Операцію відхилено. Перевірте введені дані, достатність коштів на рахунку та повторіть операцію.",
        'bank/account': "Операцію відхилено. Перевірте введені дані, достатність коштів на рахунку та повторіть операцію.",
        'bank/limit': "Операцію відхилено. Перевірте введені дані, достатність коштів на рахунку та повторіть операцію.",
        'bank/timeout': "Операцію відхилено. Перевірте введені дані, достатність коштів на рахунку та повторіть операцію.",
        'system/black-list': "Операцію відхилено. Перевірте введені дані, достатність коштів на рахунку та повторіть операцію.",
        'system/max_attempts': "Операцію відхилено. Перевірте введені дані, достатність коштів на рахунку та повторіть операцію.",
        'system/in_progress': "",
        'system/network': "Операцію відхилено. Перевірте введені дані, достатність коштів на рахунку та повторіть операцію.",
        'system/fraud': "Операцію відхилено. Перевірте введені дані, достатність коштів на рахунку та повторіть операцію.",
        'system/unavailable_method': "Операцію відхилено. Перевірте введені дані, достатність коштів на рахунку та повторіть операцію.",
        'system/operator': "Операцію відхилено. Перевірте введені дані, достатність коштів на рахунку та повторіть операцію.",
        'system/common': "Операцію відхилено. Перевірте введені дані, достатність коштів на рахунку та повторіть операцію.",
        'system/timeout': "Операцію відхилено. Перевірте введені дані, достатність коштів на рахунку та повторіть операцію.",
        'system/session': "Операцію відхилено. Перевірте введені дані, достатність коштів на рахунку та повторіть операцію.",
        'system/denied': "Операцію відхилено. Перевірте введені дані, достатність коштів на рахунку та повторіть операцію.",
        'system/already_processed': "Операцію відхилено. Перевірте введені дані, достатність коштів на рахунку та повторіть операцію.",
        'system/cancel_denied': "Операцію відхилено. Перевірте введені дані, достатність коштів на рахунку та повторіть операцію.",
        'user/timeout': "Операцію відхилено. Перевірте введені дані, достатність коштів на рахунку та повторіть операцію.",
        'user/cancel': "Операцію відхилено. Перевірте введені дані, достатність коштів на рахунку та повторіть операцію.",
        'user/duplicate': "Операцію відхилено. Перевірте введені дані, достатність коштів на рахунку та повторіть операцію.",
        'user/network': "Операцію відхилено. Перевірте введені дані, достатність коштів на рахунку та повторіть операцію.",
        'user/card_not_binded': "Операцію відхилено. Перевірте введені дані, достатність коштів на рахунку та повторіть операцію.",
        'user/unsupported_card': "Операцію відхилено. Перевірте введені дані, достатність коштів на рахунку та повторіть операцію.",
        'user/interaction_timeout': "Операцію відхилено. Перевірте введені дані, достатність коштів на рахунку та повторіть операцію.",
        'default': "Операцію відхилено. Перевірте введені дані, достатність коштів на рахунку та повторіть операцію.",
    },
    'de': {
        '3dsecure/reject': "Betrieb ist nicht möglich. Authentifizierung des Karteninhabers fehlgeschlagen.",
        '3dsecure/failed': "Betrieb ist nicht möglich. Authentifizierung des Karteninhabers fehlgeschlagen.",
        '3dsecure/timeout': "Betrieb ist nicht möglich. Authentifizierung des Karteninhabers fehlgeschlagen.",
        '3dsecure/network': "Betrieb ist nicht möglich. Authentifizierung des Karteninhabers fehlgeschlagen.",
        'system/ok': "",
        'bank/common': "Vorgang abgelehnt. Überprüfen Sie die eingegebenen Daten, die ausreichende Deckung des Kontos und wiederholen Sie den Vorgang.",
        'bank/fraud': "Vorgang abgelehnt. Überprüfen Sie die eingegebenen Daten, die ausreichende Deckung des Kontos und wiederholen Sie den Vorgang.",
        'bank/network': "Vorgang abgelehnt. Überprüfen Sie die eingegebenen Daten, die ausreichende Deckung des Kontos und wiederholen Sie den Vorgang.",
        'bank/funds': "Vorgang abgelehnt. Überprüfen Sie die eingegebenen Daten, die ausreichende Deckung des Kontos und wiederholen Sie den Vorgang.",
        'bank/account': "Vorgang abgelehnt. Überprüfen Sie die eingegebenen Daten, die ausreichende Deckung des Kontos und wiederholen Sie den Vorgang.",
        'bank/limit': "Vorgang abgelehnt. Überprüfen Sie die eingegebenen Daten, die ausreichende Deckung des Kontos und wiederholen Sie den Vorgang.",
        'bank/timeout': "Vorgang abgelehnt. Überprüfen Sie die eingegebenen Daten, die ausreichende Deckung des Kontos und wiederholen Sie den Vorgang.",
        'system/black-list': "Vorgang abgelehnt. Überprüfen Sie die eingegebenen Daten, die ausreichende Deckung des Kontos und wiederholen Sie den Vorgang.",
        'system/max_attempts': "Vorgang abgelehnt. Überprüfen Sie die eingegebenen Daten, die ausreichende Deckung des Kontos und wiederholen Sie den Vorgang.",
        'system/in_progress': "",
        'system/network': "Vorgang abgelehnt. Überprüfen Sie die eingegebenen Daten, die ausreichende Deckung des Kontos und wiederholen Sie den Vorgang.",
        'system/fraud': "Vorgang abgelehnt. Überprüfen Sie die eingegebenen Daten, die ausreichende Deckung des Kontos und wiederholen Sie den Vorgang.",
        'system/unavailable_method': "Vorgang abgelehnt. Überprüfen Sie die eingegebenen Daten, die ausreichende Deckung des Kontos und wiederholen Sie den Vorgang.",
        'system/operator': "Vorgang abgelehnt. Überprüfen Sie die eingegebenen Daten, die ausreichende Deckung des Kontos und wiederholen Sie den Vorgang.",
        'system/common': "Vorgang abgelehnt. Überprüfen Sie die eingegebenen Daten, die ausreichende Deckung des Kontos und wiederholen Sie den Vorgang.",
        'system/timeout': "Vorgang abgelehnt. Überprüfen Sie die eingegebenen Daten, die ausreichende Deckung des Kontos und wiederholen Sie den Vorgang.",
        'system/session': "Vorgang abgelehnt. Überprüfen Sie die eingegebenen Daten, die ausreichende Deckung des Kontos und wiederholen Sie den Vorgang.",
        'system/denied': "Vorgang abgelehnt. Überprüfen Sie die eingegebenen Daten, die ausreichende Deckung des Kontos und wiederholen Sie den Vorgang.",
        'system/already_processed': "Vorgang abgelehnt. Überprüfen Sie die eingegebenen Daten, die ausreichende Deckung des Kontos und wiederholen Sie den Vorgang.",
        'system/cancel_denied': "Vorgang abgelehnt. Überprüfen Sie die eingegebenen Daten, die ausreichende Deckung des Kontos und wiederholen Sie den Vorgang.",
        'user/timeout': "Vorgang abgelehnt. Überprüfen Sie die eingegebenen Daten, die ausreichende Deckung des Kontos und wiederholen Sie den Vorgang.",
        'user/cancel': "Vorgang abgelehnt. Überprüfen Sie die eingegebenen Daten, die ausreichende Deckung des Kontos und wiederholen Sie den Vorgang.",
        'user/duplicate': "Vorgang abgelehnt. Überprüfen Sie die eingegebenen Daten, die ausreichende Deckung des Kontos und wiederholen Sie den Vorgang.",
        'user/network': "Vorgang abgelehnt. Überprüfen Sie die eingegebenen Daten, die ausreichende Deckung des Kontos und wiederholen Sie den Vorgang.",
        'user/card_not_binded': "Vorgang abgelehnt. Überprüfen Sie die eingegebenen Daten, die ausreichende Deckung des Kontos und wiederholen Sie den Vorgang.",
        'user/unsupported_card': "Vorgang abgelehnt. Überprüfen Sie die eingegebenen Daten, die ausreichende Deckung des Kontos und wiederholen Sie den Vorgang.",
        'user/interaction_timeout': "Vorgang abgelehnt. Überprüfen Sie die eingegebenen Daten, die ausreichende Deckung des Kontos und wiederholen Sie den Vorgang.",
        'default': "Vorgang abgelehnt. Überprüfen Sie die eingegebenen Daten, die ausreichende Deckung des Kontos und wiederholen Sie den Vorgang.",
    },
    'fr': {
        '3dsecure/reject': "L'opération n'est pas possible. L'authentification du titulaire de la carte a échoué.",
        '3dsecure/failed': "L'opération n'est pas possible. L'authentification du titulaire de la carte a échoué.",
        '3dsecure/timeout': "L'opération n'est pas possible. L'authentification du titulaire de la carte a échoué.",
        '3dsecure/network': "L'opération n'est pas possible. L'authentification du titulaire de la carte a échoué.",
        'system/ok': "",
        'bank/common': "Opération refusée. Vérifiez les données saisies, la suffisance des fonds sur le compte et répétez l'opération.",
        'bank/fraud': "Opération refusée. Vérifiez les données saisies, la suffisance des fonds sur le compte et répétez l'opération.",
        'bank/network': "Opération refusée. Vérifiez les données saisies, la suffisance des fonds sur le compte et répétez l'opération.",
        'bank/funds': "Opération refusée. Vérifiez les données saisies, la suffisance des fonds sur le compte et répétez l'opération.",
        'bank/account': "Opération refusée. Vérifiez les données saisies, la suffisance des fonds sur le compte et répétez l'opération.",
        'bank/limit': "Opération refusée. Vérifiez les données saisies, la suffisance des fonds sur le compte et répétez l'opération.",
        'bank/timeout': "Opération refusée. Vérifiez les données saisies, la suffisance des fonds sur le compte et répétez l'opération.",
        'system/black-list': "Opération refusée. Vérifiez les données saisies, la suffisance des fonds sur le compte et répétez l'opération.",
        'system/max_attempts': "Opération refusée. Vérifiez les données saisies, la suffisance des fonds sur le compte et répétez l'opération.",
        'system/in_progress': "",
        'system/network': "Opération refusée. Vérifiez les données saisies, la suffisance des fonds sur le compte et répétez l'opération.",
        'system/fraud': "Opération refusée. Vérifiez les données saisies, la suffisance des fonds sur le compte et répétez l'opération.",
        'system/unavailable_method': "Opération refusée. Vérifiez les données saisies, la suffisance des fonds sur le compte et répétez l'opération.",
        'system/operator': "Opération refusée. Vérifiez les données saisies, la suffisance des fonds sur le compte et répétez l'opération.",
        'system/common': "Opération refusée. Vérifiez les données saisies, la suffisance des fonds sur le compte et répétez l'opération.",
        'system/timeout': "Opération refusée. Vérifiez les données saisies, la suffisance des fonds sur le compte et répétez l'opération.",
        'system/session': "Opération refusée. Vérifiez les données saisies, la suffisance des fonds sur le compte et répétez l'opération.",
        'system/denied': "Opération refusée. Vérifiez les données saisies, la suffisance des fonds sur le compte et répétez l'opération.",
        'system/already_processed': "Opération refusée. Vérifiez les données saisies, la suffisance des fonds sur le compte et répétez l'opération.",
        'system/cancel_denied': "Opération refusée. Vérifiez les données saisies, la suffisance des fonds sur le compte et répétez l'opération.",
        'user/timeout': "Opération refusée. Vérifiez les données saisies, la suffisance des fonds sur le compte et répétez l'opération.",
        'user/cancel': "Opération refusée. Vérifiez les données saisies, la suffisance des fonds sur le compte et répétez l'opération.",
        'user/duplicate': "Opération refusée. Vérifiez les données saisies, la suffisance des fonds sur le compte et répétez l'opération.",
        'user/network': "Opération refusée. Vérifiez les données saisies, la suffisance des fonds sur le compte et répétez l'opération.",
        'user/card_not_binded': "Opération refusée. Vérifiez les données saisies, la suffisance des fonds sur le compte et répétez l'opération.",
        'user/unsupported_card': "Opération refusée. Vérifiez les données saisies, la suffisance des fonds sur le compte et répétez l'opération.",
        'user/interaction_timeout': "Opération refusée. Vérifiez les données saisies, la suffisance des fonds sur le compte et répétez l'opération.",
        'default': "Opération refusée. Vérifiez les données saisies, la suffisance des fonds sur le compte et répétez l'opération.",
    },
    'es': {
        '3dsecure/reject': "La operación no es posible. La autenticación del titular de la tarjeta falló.",
        '3dsecure/failed': "La operación no es posible. La autenticación del titular de la tarjeta falló.",
        '3dsecure/timeout': "La operación no es posible. La autenticación del titular de la tarjeta falló.",
        '3dsecure/network': "La operación no es posible. La autenticación del titular de la tarjeta falló.",
        'system/ok': "",
        'bank/common': "Operación rechazada. Verifique los datos ingresados, la suficiencia de fondos en la cuenta y repita la operación.",
        'bank/fraud': "Operación rechazada. Verifique los datos ingresados, la suficiencia de fondos en la cuenta y repita la operación.",
        'bank/network': "Operación rechazada. Verifique los datos ingresados, la suficiencia de fondos en la cuenta y repita la operación.",
        'bank/funds': "Operación rechazada. Verifique los datos ingresados, la suficiencia de fondos en la cuenta y repita la operación.",
        'bank/account': "Operación rechazada. Verifique los datos ingresados, la suficiencia de fondos en la cuenta y repita la operación.",
        'bank/limit': "Operación rechazada. Verifique los datos ingresados, la suficiencia de fondos en la cuenta y repita la operación.",
        'bank/timeout': "Operación rechazada. Verifique los datos ingresados, la suficiencia de fondos en la cuenta y repita la operación.",
        'system/black-list': "Operación rechazada. Verifique los datos ingresados, la suficiencia de fondos en la cuenta y repita la operación.",
        'system/max_attempts': "Operación rechazada. Verifique los datos ingresados, la suficiencia de fondos en la cuenta y repita la operación.",
        'system/in_progress': "",
        'system/network': "Operación rechazada. Verifique los datos ingresados, la suficiencia de fondos en la cuenta y repita la operación.",
        'system/fraud': "Operación rechazada. Verifique los datos ingresados, la suficiencia de fondos en la cuenta y repita la operación.",
        'system/unavailable_method': "Operación rechazada. Verifique los datos ingresados, la suficiencia de fondos en la cuenta y repita la operación.",
        'system/operator': "Operación rechazada. Verifique los datos ingresados, la suficiencia de fondos en la cuenta y repita la operación.",
        'system/common': "Operación rechazada. Verifique los datos ingresados, la suficiencia de fondos en la cuenta y repita la operación.",
        'system/timeout': "Operación rechazada. Verifique los datos ingresados, la suficiencia de fondos en la cuenta y repita la operación.",
        'system/session': "Operación rechazada. Verifique los datos ingresados, la suficiencia de fondos en la cuenta y repita la operación.",
        'system/denied': "Operación rechazada. Verifique los datos ingresados, la suficiencia de fondos en la cuenta y repita la operación.",
        'system/already_processed': "Operación rechazada. Verifique los datos ingresados, la suficiencia de fondos en la cuenta y repita la operación.",
        'system/cancel_denied': "Operación rechazada. Verifique los datos ingresados, la suficiencia de fondos en la cuenta y repita la operación.",
        'user/timeout': "Operación rechazada. Verifique los datos ingresados, la suficiencia de fondos en la cuenta y repita la operación.",
        'user/cancel': "Operación rechazada. Verifique los datos ingresados, la suficiencia de fondos en la cuenta y repita la operación.",
        'user/duplicate': "Operación rechazada. Verifique los datos ingresados, la suficiencia de fondos en la cuenta y repita la operación.",
        'user/network': "Operación rechazada. Verifique los datos ingresados, la suficiencia de fondos en la cuenta y repita la operación.",
        'user/card_not_binded': "Operación rechazada. Verifique los datos ingresados, la suficiencia de fondos en la cuenta y repita la operación.",
        'user/unsupported_card': "Operación rechazada. Verifique los datos ingresados, la suficiencia de fondos en la cuenta y repita la operación.",
        'user/interaction_timeout': "Operación rechazada. Verifique los datos ingresados, la suficiencia de fondos en la cuenta y repita la operación.",
        'default': "Operación rechazada. Verifique los datos ingresados, la suficiencia de fondos en la cuenta y repita la operación.",
    },
    'kz': {
        '3dsecure/reject': "Операция мүмкін емес. Карта иесінің аутентификациясы орындалмады.",
        '3dsecure/failed': "Операция мүмкін емес. Карта иесінің аутентификациясы орындалмады.",
        '3dsecure/timeout': "Операция мүмкін емес. Карта иесінің аутентификациясы орындалмады.",
        '3dsecure/network': "Операция мүмкін емес. Карта иесінің аутентификациясы орындалмады.",
        'system/ok': "",
        'bank/common': "Операция қабылданбады. Енгізілген деректерді, шоттағы қаражаттың жеткіліктілігін тексеріп, операцияны қайталаңыз.",
        'bank/fraud': "Операция қабылданбады. Енгізілген деректерді, шоттағы қаражаттың жеткіліктілігін тексеріп, операцияны қайталаңыз.",
        'bank/network': "Операция қабылданбады. Енгізілген деректерді, шоттағы қаражаттың жеткіліктілігін тексеріп, операцияны қайталаңыз.",
        'bank/funds': "Операция қабылданбады. Енгізілген деректерді, шоттағы қаражаттың жеткіліктілігін тексеріп, операцияны қайталаңыз.",
        'bank/account': "Операция қабылданбады. Енгізілген деректерді, шоттағы қаражаттың жеткіліктілігін тексеріп, операцияны қайталаңыз.",
        'bank/limit': "Операция қабылданбады. Енгізілген деректерді, шоттағы қаражаттың жеткіліктілігін тексеріп, операцияны қайталаңыз.",
        'bank/timeout': "Операция қабылданбады. Енгізілген деректерді, шоттағы қаражаттың жеткіліктілігін тексеріп, операцияны қайталаңыз.",
        'system/black-list': "Операция қабылданбады. Енгізілген деректерді, шоттағы қаражаттың жеткіліктілігін тексеріп, операцияны қайталаңыз.",
        'system/max_attempts': "Операция қабылданбады. Енгізілген деректерді, шоттағы қаражаттың жеткіліктілігін тексеріп, операцияны қайталаңыз.",
        'system/in_progress': "",
        'system/network': "Операция қабылданбады. Енгізілген деректерді, шоттағы қаражаттың жеткіліктілігін тексеріп, операцияны қайталаңыз.",
        'system/fraud': "Операция қабылданбады. Енгізілген деректерді, шоттағы қаражаттың жеткіліктілігін тексеріп, операцияны қайталаңыз.",
        'system/unavailable_method': "Операция қабылданбады. Енгізілген деректерді, шоттағы қаражаттың жеткіліктілігін тексеріп, операцияны қайталаңыз.",
        'system/operator': "Операция қабылданбады. Енгізілген деректерді, шоттағы қаражаттың жеткіліктілігін тексеріп, операцияны қайталаңыз.",
        'system/common': "Операция қабылданбады. Енгізілген деректерді, шоттағы қаражаттың жеткіліктілігін тексеріп, операцияны қайталаңыз.",
        'system/timeout': "Операция қабылданбады. Енгізілген деректерді, шоттағы қаражаттың жеткіліктілігін тексеріп, операцияны қайталаңыз.",
        'system/session': "Операция қабылданбады. Енгізілген деректерді, шоттағы қаражаттың жеткіліктілігін тексеріп, операцияны қайталаңыз.",
        'system/denied': "Операция қабылданбады. Енгізілген деректерді, шоттағы қаражаттың жеткіліктілігін тексеріп, операцияны қайталаңыз.",
        'system/already_processed': "Операция қабылданбады. Енгізілген деректерді, шоттағы қаражаттың жеткіліктілігін тексеріп, операцияны қайталаңыз.",
        'system/cancel_denied': "Операция қабылданбады. Енгізілген деректерді, шоттағы қаражаттың жеткіліктілігін тексеріп, операцияны қайталаңыз.",
        'user/timeout': "Операция қабылданбады. Енгізілген деректерді, шоттағы қаражаттың жеткіліктілігін тексеріп, операцияны қайталаңыз.",
        'user/cancel': "Операция қабылданбады. Енгізілген деректерді, шоттағы қаражаттың жеткіліктілігін тексеріп, операцияны қайталаңыз.",
        'user/duplicate': "Операция қабылданбады. Енгізілген деректерді, шоттағы қаражаттың жеткіліктілігін тексеріп, операцияны қайталаңыз.",
        'user/network': "Операция қабылданбады. Енгізілген деректерді, шоттағы қаражаттың жеткіліктілігін тексеріп, операцияны қайталаңыз.",
        'user/card_not_binded': "Операция қабылданбады. Енгізілген деректерді, шоттағы қаражаттың жеткіліктілігін тексеріп, операцияны қайталаңыз.",
        'user/unsupported_card': "Операция қабылданбады. Енгізілген деректерді, шоттағы қаражаттың жеткіліктілігін тексеріп, операцияны қайталаңыз.",
        'user/interaction_timeout': "Операция қабылданбады. Енгізілген деректерді, шоттағы қаражаттың жеткіліктілігін тексеріп, операцияны қайталаңыз.",
        'default': "Операция қабылданбады. Енгізілген деректерді, шоттағы қаражаттың жеткіліктілігін тексеріп, операцияны қайталаңыз.",
    },
    'it': {
        '3dsecure/reject': "L'operazione non è possibile. Autenticazione del titolare della carta non riuscita.",
        '3dsecure/failed': "L'operazione non è possibile. Autenticazione del titolare della carta non riuscita.",
        '3dsecure/timeout': "L'operazione non è possibile. Autenticazione del titolare della carta non riuscita.",
        '3dsecure/network': "L'operazione non è possibile. Autenticazione del titolare della carta non riuscita.",
        'system/ok': "",
        'bank/common': "Operazione rifiutata. Controlla i dati inseriti, la sufficienza dei fondi sul conto e ripeti l'operazione.",
        'bank/fraud': "Operazione rifiutata. Controlla i dati inseriti, la sufficienza dei fondi sul conto e ripeti l'operazione.",
        'bank/network': "Operazione rifiutata. Controlla i dati inseriti, la sufficienza dei fondi sul conto e ripeti l'operazione.",
        'bank/funds': "Operazione rifiutata. Controlla i dati inseriti, la sufficienza dei fondi sul conto e ripeti l'operazione.",
        'bank/account': "Operazione rifiutata. Controlla i dati inseriti, la sufficienza dei fondi sul conto e ripeti l'operazione.",
        'bank/limit': "Operazione rifiutata. Controlla i dati inseriti, la sufficienza dei fondi sul conto e ripeti l'operazione.",
        'bank/timeout': "Operazione rifiutata. Controlla i dati inseriti, la sufficienza dei fondi sul conto e ripeti l'operazione.",
        'system/black-list': "Operazione rifiutata. Controlla i dati inseriti, la sufficienza dei fondi sul conto e ripeti l'operazione.",
        'system/max_attempts': "Operazione rifiutata. Controlla i dati inseriti, la sufficienza dei fondi sul conto e ripeti l'operazione.",
        'system/in_progress': "",
        'system/network': "Operazione rifiutata. Controlla i dati inseriti, la sufficienza dei fondi sul conto e ripeti l'operazione.",
        'system/fraud': "Operazione rifiutata. Controlla i dati inseriti, la sufficienza dei fondi sul conto e ripeti l'operazione.",
        'system/unavailable_method': "Operazione rifiutata. Controlla i dati inseriti, la sufficienza dei fondi sul conto e ripeti l'operazione.",
        'system/operator': "Operazione rifiutata. Controlla i dati inseriti, la sufficienza dei fondi sul conto e ripeti l'operazione.",
        'system/common': "Operazione rifiutata. Controlla i dati inseriti, la sufficienza dei fondi sul conto e ripeti l'operazione.",
        'system/timeout': "Operazione rifiutata. Controlla i dati inseriti, la sufficienza dei fondi sul conto e ripeti l'operazione.",
        'system/session': "Operazione rifiutata. Controlla i dati inseriti, la sufficienza dei fondi sul conto e ripeti l'operazione.",
        'system/denied': "Operazione rifiutata. Controlla i dati inseriti, la sufficienza dei fondi sul conto e ripeti l'operazione.",
        'system/already_processed': "Operazione rifiutata. Controlla i dati inseriti, la sufficienza dei fondi sul conto e ripeti l'operazione.",
        'system/cancel_denied': "Operazione rifiutata. Controlla i dati inseriti, la sufficienza dei fondi sul conto e ripeti l'operazione.",
        'user/timeout': "Operazione rifiutata. Controlla i dati inseriti, la sufficienza dei fondi sul conto e ripeti l'operazione.",
        'user/cancel': "Operazione rifiutata. Controlla i dati inseriti, la sufficienza dei fondi sul conto e ripeti l'operazione.",
        'user/duplicate': "Operazione rifiutata. Controlla i dati inseriti, la sufficienza dei fondi sul conto e ripeti l'operazione.",
        'user/network': "Operazione rifiutata. Controlla i dati inseriti, la sufficienza dei fondi sul conto e ripeti l'operazione.",
        'user/card_not_binded': "Operazione rifiutata. Controlla i dati inseriti, la sufficienza dei fondi sul conto e ripeti l'operazione.",
        'user/unsupported_card': "Operazione rifiutata. Controlla i dati inseriti, la sufficienza dei fondi sul conto e ripeti l'operazione.",
        'user/interaction_timeout': "Operazione rifiutata. Controlla i dati inseriti, la sufficienza dei fondi sul conto e ripeti l'operazione.",
        'default': "Operazione rifiutata. Controlla i dati inseriti, la sufficienza dei fondi sul conto e ripeti l'operazione.",
    },
    'zh': {
        '3dsecure/reject': u'无法操作。 持卡人身份验证失败。\n',
        '3dsecure/failed': u'无法操作。 持卡人身份验证失败。\n',
        '3dsecure/timeout': u'无法操作。 持卡人身份验证失败。\n',
        '3dsecure/network': u'无法操作。 持卡人身份验证失败。\n',
        'system/ok': u'\n',
        'bank/common': u'操作被拒绝。 检查输入的数据，账户上的资金是否充足，然后重复操作。\n',
        'bank/fraud': u'操作被拒绝。 检查输入的数据，账户上的资金是否充足，然后重复操作。\n',
        'bank/network': u'操作被拒绝。 检查输入的数据，账户上的资金是否充足，然后重复操作。\n',
        'bank/funds': u'操作被拒绝。 检查输入的数据，账户上的资金是否充足，然后重复操作。\n',
        'bank/account': u'操作被拒绝。 检查输入的数据，账户上的资金是否充足，然后重复操作。\n',
        'bank/limit': u'操作被拒绝。 检查输入的数据，账户上的资金是否充足，然后重复操作。\n',
        'bank/timeout': u'操作被拒绝。 检查输入的数据，账户上的资金是否充足，然后重复操作。\n',
        'system/black-list': u'操作被拒绝。 检查输入的数据，账户上的资金是否充足，然后重复操作。\n',
        'system/max_attempts': u'操作被拒绝。 检查输入的数据，账户上的资金是否充足，然后重复操作。\n',
        'system/in_progress': u'\n',
        'system/network': u'操作被拒绝。 检查输入的数据，账户上的资金是否充足，然后重复操作。',
        'system/fraud': u'操作被拒绝。 检查输入的数据，账户上的资金是否充足，然后重复操作。',
        'system/unavailable_method': u'操作被拒绝。 检查输入的数据，账户上的资金是否充足，然后重复操作。',
        'system/operator': u'操作被拒绝。 检查输入的数据，账户上的资金是否充足，然后重复操作。',
        'system/common': u'操作被拒绝。 检查输入的数据，账户上的资金是否充足，然后重复操作。',
        'system/timeout': u'操作被拒绝。 检查输入的数据，账户上的资金是否充足，然后重复操作。',
        'system/session': u'操作被拒绝。 检查输入的数据，账户上的资金是否充足，然后重复操作。',
        'system/denied': u'操作被拒绝。 检查输入的数据，账户上的资金是否充足，然后重复操作。',
        'system/already_processed': u'操作被拒绝。 检查输入的数据，账户上的资金是否充足，然后重复操作。',
        'system/cancel_denied': u'操作被拒绝。 检查输入的数据，账户上的资金是否充足，然后重复操作。',
        'user/timeout': u'操作被拒绝。 检查输入的数据，账户上的资金是否充足，然后重复操作。',
        'user/cancel': u'操作被拒绝。 检查输入的数据，账户上的资金是否充足，然后重复操作。',
        'user/duplicate': u'操作被拒绝。 检查输入的数据，账户上的资金是否充足，然后重复操作。',
        'user/network': u'操作被拒绝。 检查输入的数据，账户上的资金是否充足，然后重复操作。',
        'user/card_not_binded': u'操作被拒绝。 检查输入的数据，账户上的资金是否充足，然后重复操作。',
        'user/unsupported_card': u'操作被拒绝。 检查输入的数据，账户上的资金是否充足，然后重复操作。',
        'user/interaction_timeout': u'操作被拒绝。 检查输入的数据，账户上的资金是否充足，然后重复操作。',
        'default': u'操作被拒绝。 检查输入的数据，账户上的资金是否充足，然后重复操作。',
    },
}
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
    "en": {
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
    "ua": {
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
    "de": {
        "organisation": "Organisation",
        "date": "Datum",
        "order_number": "Auftragsnummer",
        "amount": "Zahlungsbetrag",
        "commission": "Zahlungsprovision",
        "cardnumber": "Kartennummer",
        "cardholder": "Karteninhaber",
        "terminal": "Terminal ID",
        "refnum": "Refnum",
        "auth_code": "Autorisierungscode",
    },
    "fr": {
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
    "es": {
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
    "kz": {
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
    "it": {
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
    "zh": {
        "organization": "Organisation",
        "date": "Date",
        "terminal": "ID",
        "refnum": "Refnum",
    }
}

coordinates_by_language = {
    "ru": {
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
    "en": {
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
    "ua": {
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
    },
    "de": {
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
    },
    "fr": {
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
    },
    "es": {
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
    },
    "kz": {
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
    },
    "it": {
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
    },
    "zh": {
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
            # imagePath = '/usr/lib/python2.7/dist-packages/ego_auth/lib/cheque_pdf/alfabank_logo.png'
            imagePath = path.abspath('alfabank_logo.png')
            self.image(imagePath, centeredImage, 34, 33.3, 9.4)
        else:
            # imagePath = '/usr/lib/python2.7/dist-packages/ego_auth/lib/cheque_pdf/alfabank_logo_eng.png'
            imagePath = path.abspath('alfabank_logo_eng.png')
            self.image(imagePath, centeredImage, 34, 6, 9.4)
        self.cell(w=50, align='C', border=0)

    def setTitle(self, labels, cords, data, language):
        self.set_xy(24.5, cords.get("header", ""))
        self.set_font('Bold', '', 16.8)
        self.set_text_color(0, 0, 0)
        self.cell(w=160, align='L', ln=1, txt=labels.get("header", ""), border=0)

        # organization
        self.set_xy(24.5, cords.get("organization", ""))
        self.set_font('Regular', '', 13.6)
        self.cell(w=80, align='L', txt=labels.get("organization", ""), border=0)

        self.set_xy(110.5, cords.get("organization", ""))
        self.cell(w=80, align='L', txt=data['organization'], border=0)

        # date_of_payment
        self.set_xy(24.5, cords.get("date", ""))
        self.cell(w=80, align='L', txt=labels.get("date", ""), border=0)

        self.set_xy(110.5, cords.get("date", ""))
        self.cell(w=80, align='L', txt=data['date_of_payment'], border=0)

        # order_number
        self.set_xy(24.5, cords.get("order_number", ""))
        self.cell(w=80, align='L', txt=labels.get("order_number", ""), border=0)

        self.set_xy(110.5, cords.get("order_number", ""))
        self.cell(w=80, align='L', txt=data['order_number'], border=0)

        # amount_of_payment
        self.set_xy(24.5, cords.get("amount", ""))
        self.cell(w=80, align='L', txt=labels.get("amount", ""), border=0)

        self.set_xy(110.5, cords.get("amount", ""))
        self.cell(w=80, align='L', txt=data['amount_of_payment'], border=0)

        # payment_commission
        self.set_xy(24.5, cords.get("commission", ""))
        self.cell(w=80, align='L', txt=labels.get("commission", ""), border=0)

        self.set_xy(110.5, cords.get("commission", ""))
        self.cell(w=80, align='L', txt=data['payment_commission'], border=0)

        # card_number
        self.set_xy(24.5, cords.get("cardnumber", ""))
        self.cell(w=80, align='L', txt=labels.get("cardnumber", ""), border=0)

        self.set_xy(110.5, cords.get("cardnumber", ""))
        self.cell(w=80, align='L', txt=data['card_number'], border=0)

        # name
        self.set_xy(24.5, cords.get("cardholder", ""))
        self.cell(w=80, align='L', txt=labels.get("cardholder", ""), border=0)

        self.set_xy(110.5, cords.get("cardholder", ""))
        self.cell(w=80, align='L', txt=data['name'], border=0)

        # terminal_id
        self.set_xy(24.5, cords.get("terminal", ""))
        self.cell(w=80, align='L', txt=labels.get("terminal", ""), border=0)

        self.set_xy(110.5, cords.get("terminal", ""))
        self.cell(w=80, align='L', txt=data['terminal_id'], border=0)

        # refnum
        self.set_xy(24.5, cords.get("refnum", ""))
        self.cell(w=80, align='L', txt=labels.get("refnum", ""), border=0)

        self.set_xy(110.5, cords.get("refnum", ""))
        self.cell(w=80, align='L', txt=data['refnum'], border=0)

        # auth_code
        self.set_xy(24.5, cords.get("auth_code", ""))
        self.cell(w=80, align='L', txt=labels.get("auth_code", ""), border=0)

        self.set_xy(110.5, cords.get("auth_code", ""))
        self.cell(w=80, align='L', txt=data['auth_code'], border=0)

        if data['rejection']:
            if labels.get('fail_reasone'):
                self.set_xy(13.8, cords.get("reasone_title", ""))
                self.set_font('Bold', '', 14)
                self.multi_cell(w=170, h=6, align='L', txt=labels.get('fail_reasone', ''), border=0)

            if language == 'zh':
                self.set_xy(13.8, cords.get("fail_reasone", ""))
                self.set_font('AdditionalChinese', '', 14)
                # self.write(8, u'Chinese: 你好世界\n')
                # self.write(8, u'操作被拒絕。 檢查輸入的數據，賬戶上的資金是否充足，然後重複操作。\n')
                self.write(8, data['rejection'])
                # self.multi_cell(w=170, h=6, align='L', txt=data['rejection'], border=0)
            else:
                self.set_xy(13.8, cords.get("fail_reasone", ""))
                self.set_font('Regular', '', 12)
                self.multi_cell(w=170, h=6, align='L', txt=data['rejection'], border=0)


def create_pdf_cheque(data, language):
    labels = labels_by_language[language]
    if data['success']:
        labels["header"] = labels.get("success_header", "")
    else:
        labels["header"] = labels.get("fail_header", "")

    if data['rejection']:
        data['rejection'] = reasonMap[language].get(data['rejection'], reasonMap[language]["default"])

    cords = coordinates_by_language[language]
    # path to font
    # fontPathRegular = '/usr/lib/python2.7/dist-packages/ego_auth/lib/cheque_pdf/ArialMT-Regular.ttf'
    fontPathRegular = path.abspath('ArialMT-Regular.ttf')
    # fontPathBold = '/usr/lib/python2.7/dist-packages/ego_auth/lib/cheque_pdf/Arial-Bold.ttf'
    fontPathBold = path.abspath('Arial-Bold.ttf')
    # fontPathBold = '/usr/lib/python2.7/dist-packages/ego_auth/lib/cheque_pdf/AdditionalChineesse.ttf'
    AdditionalChinese = path.abspath('AdditionalChinese.ttf')
    # generate class
    pdf = PDF('P', 'mm', [216, 279])
    # add Roboto font
    pdf.add_font('Regular', '', fontPathRegular, uni=True)
    pdf.add_font('Bold', '', fontPathBold, uni=True)
    if language == 'zh':
        pdf.add_font('AdditionalChinese', '', AdditionalChinese, uni=True)
    # create page
    pdf.add_page()
    # set title on page
    pdf.setTitle(labels, cords, data, language)
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

create_pdf_cheque(dataDict, 'zh')