## **Django Signals**

### **Question 1: Are Django signals executed synchronously or asynchronously by default?**

By default, Django signals are executed **synchronously**. This means the signal handler completes execution before the caller's next line is executed.

### **Question 2: Do Django signals run in the same thread as the caller?**

Yes, Django signals run in the **same thread** as the caller by default.

### **Question 3: Do Django signals run in the same database transaction as the caller?**

By default, Django signals run in the **same database transaction** as the caller. If the transaction fails, changes in the signal are also rolled back.

---

## **Custom Classes in Python**

### **Description: Create a Rectangle Class**

**Requirements**:
1. The `Rectangle` class requires `length` and `width` as initialization parameters.
2. The class should be iterable.
3. Iterating over the instance should return:
   - First: A dictionary with the key `length` and its corresponding value.
   - Second: A dictionary with the key `width` and its corresponding value.
---
Made the required class in rectangle_class.py


