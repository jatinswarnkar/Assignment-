# signalsdemo/test_signals.py
import os
import django
import time
import threading

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'signalsdemo.settings')
django.setup()

from django.db import transaction
from signals_demo.models import Order, Product, User

def test_order_signal():
    print("Testing Order Signal (Synchronous Execution)")
    start_time = time.time()
    order = Order(total=100.00)
    order.save()
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time} seconds")

def test_product_thread():
    print("Testing Product Signal (Thread Execution)")
    main_thread = threading.current_thread()
    product = Product(name="Test Product")
    product.save()

def test_transaction_signal():
    print("Testing User Signal (Transaction Execution)")
    with transaction.atomic():
        user = User(username="testuser")
        user.save()



def run_all_tests():
    test_order_signal()
    test_product_thread()
    test_transaction_signal()

if __name__ == '__main__':
    run_all_tests()