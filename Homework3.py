# Question 3 - Date Converter for Nepal Bank System (BS <-> AD)
bs_months = ["Baisakh", "Jestha", "Ashadh", "Shrawan", "Bhadra", "Ashwin",
             "Kartik", "Mangsir", "Poush", "Magh", "Falgun", "Chaitra"]

customers = [
    {"name": "Ramesh Thapa",  "date": "1985-06-24", "cal": "AD", "need": "BS", "style": "full"},
    {"name": "Sunita Karki",  "date": "2055-09-10", "cal": "BS", "need": "AD", "style": "iso"},
    {"name": "Bikash Rai",    "date": "1998-11-30", "cal": "AD", "need": "BS", "style": "nepali"},
    {"name": "Anjali Gurung", "date": "2040-01-05", "cal": "BS", "need": "AD", "style": "full"},
]
 
 
def convert_date(date_str, from_cal, to_cal):
    # if the calendars are the same, nothing to convert
    if from_cal == to_cal:
        return date_str
 
    year, month, day = date_str.split("-")
    year = int(year)
 
    # apply the 56 year offset in the correct direction
    if from_cal == "AD" and to_cal == "BS":
        year += 56
    elif from_cal == "BS" and to_cal == "AD":
        year -= 56
 
    return f"{year:04d}-{month}-{day}"
 
 
def day_suffix(day):
    # gives the right ending for a day number, like 1st, 2nd, 3rd, 4th...
    day = int(day)
    if 11 <= day <= 13:
        return "th"
    last_digit = day % 10
    if last_digit == 1:
        return "st"
    elif last_digit == 2:
        return "nd"
    elif last_digit == 3:
        return "rd"
    else:
        return "th"
 
 
def format_converted_date(converted_str, to_cal, style):
    # this just controls how the converted date looks depending on the style asked for
    year, month, day = converted_str.split("-")
 
    if to_cal == "BS" and style == "full":
        # spelled out with an ordinal suffix, e.g. "24th Ashwin, 2041 BS"
        month_name = bs_months[int(month) - 1]
        suffix = day_suffix(day)
        return f"{int(day)}{suffix} {month_name}, {year} BS"
 
    elif to_cal == "BS" and style == "nepali":
        # plainer style, no ordinal suffix or comma, e.g. "24 Ashwin 2041 BS"
        month_name = bs_months[int(month) - 1]
        return f"{int(day)} {month_name} {year} BS"
 
    else:
        # iso style, or converting to AD, just keep it as YYYY-MM-DD
        return f"{converted_str} {to_cal}"
 
 
print("QUESTION 3")
 
# runs through the given customer list first
for customer in customers:
    converted = convert_date(customer["date"], customer["cal"], customer["need"])
    formatted = format_converted_date(converted, customer["need"], customer["style"])
    print(f'{customer["name"]:<13} | Original: {customer["date"]} {customer["cal"]} | Converted: {formatted}')
 
# then lets the user try converting their own date
print("\nConvert your own date (type 'done' as the date to stop)")
while True:
    user_date = input("Date (YYYY-MM-DD): ").strip()
 
    if user_date.lower() == "done":
        break
 
    user_name = input("Name: ").strip()
    user_from = input("From calendar (AD/BS): ").strip().upper()
    user_to = input("To calendar (AD/BS): ").strip().upper()
    user_style = input("Style (full/nepali/iso): ").strip().lower()
 
    converted = convert_date(user_date, user_from, user_to)
    formatted = format_converted_date(converted, user_to, user_style)
    print(f"{user_name} | Original: {user_date} {user_from} | Converted: {formatted}")
print()
 