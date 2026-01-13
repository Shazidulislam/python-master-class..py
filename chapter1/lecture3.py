

# !! Input in python

"""
!!Input in Python
input( ) statement is used to accept values (using keyboard) from user

input( ) #result for input( ) is always a str

int(intput()) #!int 

float ( input( ) ) #float













পাইথন-এ **ইনপুট নেওয়ার** উপায় হলো `input()` ফাংশন।

### `input()` কী করে?
- `input()` ব্যবহার করে কীবোর্ড থেকে ইউজারের কাছ থেকে ভ্যালু নেওয়া হয়।
- এটি সবসময় **স্ট্রিং (str)** টাইপের ডেটা রিটার্ন করে, যদি ইউজার সংখ্যা লিখুক বা না লিখুক।

### উদাহরণ:
```python
name = input()          # ইউজার যা লিখবে তা স্ট্রিং হিসেবে সংরক্ষিত হবে
number = input()        # এখানেও স্ট্রিং হবে, এমনকি ইউজার ৫০ লিখলেও
```

### সংখ্যা হিসেবে নিতে চাইলে টাইপ কাস্ট করতে হয়

1. **ইন্টিজার (পূর্ণসংখ্যা) নেওয়ার জন্য:**
   ```python
   age = int(input())      # ইউজার যা লিখবে তা ইন্টিজারে কনভার্ট হবে
   ```
   - উদাহরণ: ইউজার ২৫ লিখলে `age` এর মান হবে ২৫ (int টাইপ)।

2. **ফ্লোট (দশমিক সংখ্যা) নেওয়ার জন্য:**
   ```python
   height = float(input()) # ইউজার যা লিখবে তা ফ্লোটে কনভার্ট হবে
   ```
   - উদাহরণ: ইউজার ৫.৯ লিখলে `height` এর মান হবে ৫.৯ (float টাইপ)।

### গুরুত্বপূর্ণ নোট:
- শুধু `input()` লিখলে সবকিছু স্ট্রিং হয়ে যায়। তাই গাণিতিক কাজ করতে চাইলে অবশ্যই `int()` বা `float()` দিয়ে কনভার্ট করতে হবে।
- যদি ইউজার সংখ্যার বদলে অক্ষর লিখে দেয় এবং আপনি `int()` বা `float()` দিয়ে কনভার্ট করার চেষ্টা করেন, তাহলে প্রোগ্রামে **Error** হবে (ValueError)।

### প্রম্পট সহ ইনপুট নেওয়া (ভালো প্র্যাকটিস):
```python
name = input("আপনার নাম লিখুন: ")
age = int(input("আপনার বয়স লিখুন: "))
```
এভাবে লিখলে ইউজার বুঝতে পারবে কী লিখতে হবে।

সংক্ষেপে:  
`input()` → সবসময় স্ট্রিং দেয়  
`int(input())` → পূর্ণসংখ্যা  
`float(input())` → দশমিক সংখ্যা
"""









# !! Input  in python



name = input("Apner name likhon : ")

print("Hello" , name);

number = int(input("Ekti Number type koron: "))
print("Your Sum : " ,number+20);

flot_number = float(input("Type flot number: "))

print("The Float Number : " , flot_number + number);