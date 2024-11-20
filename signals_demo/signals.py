import threading
import time
from django.db import models, transaction
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Order, Product, User

current_thread = None
transaction_state = []

@receiver(pre_save, sender=Order)
def log_order_creation(sender, instance, **kwargs):
    time.sleep(2)
    print(f"Signal processed for order with total: {instance.total}")

@receiver(pre_save, sender=Product)
def check_thread(sender, instance, **kwargs):
    global current_thread
    current_thread = threading.current_thread()
    print(f"Signal handler thread: {current_thread.name}")

@receiver(pre_save, sender=User)
def track_transaction(sender, instance, **kwargs):
    in_transaction = transaction.get_connection().in_atomic_block
    transaction_state.append(in_transaction)
    print(f"Signal handler in transaction: {in_transaction}")