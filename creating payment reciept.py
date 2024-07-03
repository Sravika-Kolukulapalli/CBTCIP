from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
import datetime

def create_receipt(transaction_id, date, customer_name, items, total_amount, output_filename):
    
    c = canvas.Canvas(output_filename, pagesize=letter)
    width, height = letter
    

    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2.0, height - 50, "Payment Receipt")

    
    c.setFont("Helvetica", 12)
    c.drawString(30, height - 100, f"Transaction ID: {transaction_id}")
    c.drawString(30, height - 120, f"Date: {date}")
    c.drawString(30, height - 140, f"Customer Name: {customer_name}")
    c.setFont("Helvetica-Bold", 12)
    c.drawString(30, height - 180, "Item")
    c.drawString(250, height - 180, "Quantity")
    c.drawString(350, height - 180, "Price")
    c.drawString(450, height - 180, "Total")

    
    y_position = height - 200
    c.setFont("Helvetica", 12)
    for item, quantity, price, total in items:
        c.drawString(30, y_position, item)
        c.drawString(250, y_position, str(quantity))
        c.drawString(350, y_position, f"${price:.2f}")
        c.drawString(450, y_position, f"${total:.2f}")
        y_position -= 20


    c.setFont("Helvetica-Bold", 12)
    c.drawString(350, y_position - 20, "Total Amount:")
    c.drawString(450, y_position - 20, f"${total_amount:.2f}")

    
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(30, 30, "Thank you for your business!")
    
    
    c.showPage()
    c.save()


if __name__ == "__main__":
    transaction_id = "123456789"
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    customer_name = "John Doe"
    items = [
        ("Item A", 2, 10.00, 20.00),
        ("Item B", 1, 15.00, 15.00),
        ("Item C", 3, 7.50, 22.50),
    ]
    total_amount = sum(item[3] for item in items)
    output_filename = "receipt.pdf"
    
    create_receipt(transaction_id, date, customer_name, items, total_amount, output_filename)
    print(f"Receipt saved as {output_filename}")
