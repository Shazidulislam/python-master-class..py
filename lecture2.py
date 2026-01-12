

"""
# !!Types of Operators
# ? An operator is a symbol that performs a certain operation between operands.

# !! Arithmetic Operators ( + , - , * , / , % , ** )

# **Relational / Comparison Operators ( == , != , > , < , >= , <= )

# !!Assignment Operators ( = , +=, -= ,*= , /= , %= ,**= )

# ?Logical Operators ( not , and , or )


"""

# !! Arithmetic Operators ( + , - , * , / , % ,** )

# a = 5
# b = 3

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b) #reminder
# print(a**b)  #power a^b

# **Relational / Comparison Operators ( == , != , > , < , >= , <= )

a = 20;
b = 30;

# print(a==b) #False
# print(a!=b) #True
# print(a>b) #False
# print(a<b) #True
# print(a>=b) #False
# print(a<=b) #True


# !!Assignment Operators ( = , +=, -= ,*= , /= , %= ,**= )

num = 10;
num +=10;

# print("Num : ",num);
num -= 5;

# print("Num Sub : ",num);

num *= 5;
# print("Num mul : ", num)

num /= 5;
# print("Num Div : ", num)


num %= 2;
# print("Num % : ", num)

nums =5;
nums **= 2;
# print("Nums ** : ", nums)



# !Logical Operators ( not , and , or )

# print(not False);
# print(not True);
# print(not (4>5));


"""

পাইথনে Type Conversion এবং Casting বলতে মূলত এক ধরনের ডেটা টাইপকে অন্য ডেটা টাইপে পরিবর্তন করাকে বোঝায়। যেমন: একটি Integer (পূর্ণসংখ্যা) কে Float (দশমিক সংখ্যা) এ রূপান্তর করা।

পাইথনে এটি প্রধানত দুই ভাবে হয়:

১. Implicit Type Conversion (স্বয়ংক্রিয় পরিবর্তন)
পাইথন যখন নিজে থেকেই কোনো ডেটা টাইপ পরিবর্তন করে নেয়, তখন তাকে Implicit Type Conversion বলে। এতে ইউজারের কিছু করতে হয় না এবং ডেটা লস হওয়ার সম্ভাবনা থাকে না।

উদাহরণ:

Python

num_int = 10    # Integer
num_flo = 1.5   # Float

result = num_int + num_flo
print(result)       # আউটপুট: 11.5
print(type(result)) # আউটপুট: <class 'float'>
এখানে পাইথন ছোট ডেটা টাইপ (int) কে বড় ডেটা টাইপ (float) এ নিজে থেকেই রূপান্তর করে নিয়েছে যাতে রেজাল্ট সঠিক থাকে।

২. Explicit Type Conversion বা Casting (ব্যবহারকারী দ্বারা পরিবর্তন)
যখন প্রোগ্রামার নিজে কোনো নির্দিষ্ট ফাংশন ব্যবহার করে ডেটা টাইপ পরিবর্তন করেন, তখন তাকে Casting বলে। পাইথনে এর জন্য কিছু বিল্ট-ইন ফাংশন আছে:

int(): অন্য টাইপ থেকে পূর্ণসংখ্যায় নিতে।

float(): অন্য টাইপ থেকে দশমিকে নিতে।

str(): অন্য টাইপ থেকে স্ট্রিং বা লেখায় নিতে।

উদাহরণ:

Python

# String থেকে Integer এ রূপান্তর
age_str = "25"
age_int = int(age_str) 

print(age_int + 5) # আউটপুট: 30
কেন Casting প্রয়োজন?
ইউজার যখন input() ফাংশন দিয়ে কিছু ইনপুট দেয়, পাইথন সেটাকে সবসময় String হিসেবে ধরে। এখন আপনি যদি দুটি সংখ্যার যোগফল বের করতে চান, তবে আপনাকে অবশ্যই সেগুলোকে int() বা float() এ কাস্ট করে নিতে হবে।

এক নজরে মূল পার্থক্য
বিষয়	Implicit Conversion	Explicit Conversion (Casting)
কার দ্বারা হয়	পাইথন নিজে করে	প্রোগ্রামার নিজে করেন
ফাংশন ব্যবহার	প্রয়োজন নেই	নির্দিষ্ট ফাংশন (int, float, str) লাগে
ডেটা লস	হয় না	হতে পারে (যেমন: float থেকে int করলে দশমিক অংশ বাদ যায়)

সতর্কতা: আপনি চাইলেই যেকোনো কিছুকে পরিবর্তন করতে পারবেন না। যেমন: int("Hello") দিলে পাইথন এরর (ValueError) দেখাবে, কারণ "Hello" কোনো সংখ্যা নয়।

আপনি কি পাইথনের অন্য কোনো টপিক যেমন List বা Loop নিয়ে বিস্তারিত জানতে চান?
"""

# !Type Conversion
a=2;

b=4.45;
sum = a+b; # 2.0+4.45 = 6.45

 
# !!Type Casting

"""
initger conver korte 
#!int() // character ke intiger e convert kora jai na
#*flot() // charater ke flot kora jai na 
#!str()

"""