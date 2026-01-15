
# !! stgingFunction


"""
#?ফাংশন,কাজ (Meaning in Bengali)

#!upper(),স্ট্রিং-এর সব অক্ষরকে বড় হাতের (Uppercase) করে দেয়।

#*lower(),স্ট্রিং-এর সব অক্ষরকে ছোট হাতের (Lowercase) করে দেয়।

#!capitalize(),শুধুমাত্র স্ট্রিং-এর প্রথম অক্ষরটি বড় হাতের করে।


#*title(),প্রতিটি শব্দের প্রথম অক্ষর বড় হাতের করে দেয়।

#!swapcase(),বড় হাতের অক্ষরকে ছোট এবং ছোট হাতের অক্ষরকে বড় হাতের করে।

#*strip(),স্ট্রিং-এর শুরু এবং শেষের অতিরিক্ত ফাঁকা জায়গা (Whitespace) মুছে দেয়।



#?ফাংশন,কাজ (Meaning in Bengali)

#!len(),স্ট্রিং-এ মোট কতটি অক্ষর আছে তা জানায় (Length)।

#*find(),নির্দিষ্ট কোনো অক্ষর বা শব্দ কোথায় আছে তার ইনডেক্স নম্বর জানায়। না পেলে -1 দেয়।

#!count(),কোনো নির্দিষ্ট অক্ষর বা শব্দ স্ট্রিং-এ কতবার আছে তা গুনে বের করে।

#*startswith(),স্ট্রিংটি নির্দিষ্ট কোনো শব্দ দিয়ে শুরু হয়েছে কি না তা পরীক্ষা করে (True/False)।

#! endswith(),স্ট্রিংটি নির্দিষ্ট কোনো শব্দ দিয়ে শেষ হয়েছে কি না তা পরীক্ষা করে।



#?ফাংশন,কাজ (Meaning in Bengali)

#! split(),স্ট্রিংকে নির্দিষ্ট চিহ্নের (যেমন কমা বা স্পেস) ভিত্তিতে একাধিক ভাগে ভাগ করে একটি লিস্ট তৈরি করে।

#* join(),একটি লিস্টের অনেকগুলো শব্দকে একটি নির্দিষ্ট চিহ্ন দিয়ে যুক্ত করে স্ট্রিং তৈরি করে।

#! replace(old ,new),স্ট্রিং-এর কোনো নির্দিষ্ট অংশ পরিবর্তন করে নতুন কিছু বসায়।

"""
str = "i Am studyding python from ApnaCollege!"

print(str.endswith("ege!"))
str = str.capitalize()

print(str)

print(str.replace("python" ,"C++"))

print(str.find("from"))

print(str.count("o"))

print(str.upper())



print(str.lower())

print(str.title())


print(str.swapcase())

print(len(str))