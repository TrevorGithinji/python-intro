#TC03V7DGN3 Confirmed. Ksh 3,000 sent to JOHN MARK on 24/7/25 at 8.02 AM

# message = ""

def extract_amount(mpesa_messages):
    index_Ksh = mpesa_messages.index('Ksh')
    index_sent = mpesa_messages.index('sent')
    amount = mpesa_messages[index_Ksh: index_sent]
    amount = amount.replace('Ksh', '')
    amount = amount.replace(',', '')

    print(amount)

def extract_date(mpesa_messages):
    index_on = mpesa_messages.index(" on ")
    index_at = mpesa_messages.index(" at ")
    date = mpesa_messages[index_on: index_at]
    date = date.replace("on", "")
    date = date.strip()
    print(date)

message_1 = "TC03V7DGN3 Confirmed. Ksh 3,000 sent to JOHN Simon on 24/7/25 at 8.02 AM"
extract_amount(message_1)



