import pandas as pd

# excel file load 

file_path = r"C:\Users\Dell\OneDrive\Desktop\python\project unifid\EduPro Online Platform.xlsx"

# alg alg sheet load krte hai 

users = pd.read_excel(file_path, sheet_name="Users")
teachers = pd.read_excel(file_path, sheet_name="Teachers")
courses = pd.read_excel(file_path, sheet_name="Courses")
transactions = pd.read_excel(file_path, sheet_name="Transactions")

#check krte hai 

print(users.head())

print(teachers.head())

print(courses.head())

print(transactions.head())

# ab sbhi sheets ko merge krege 

df = transactions.merge(courses,on="CourseID",how="left")
df = df.merge(teachers,on="TeacherID",how="left")
df = df.merge(users,on="UserID",how="left")

# price band 
def price_band(price):
    if price == 0:
        return "free"
    elif price < 200:
        return "low"
    elif price < 400 :
        return "medium"
    else:
        return "high"
    
df["PriceBand"] = df["CoursePrice"].apply(price_band)
print(df[["CoursePrice",'PriceBand']].head())
print(df["CoursePrice"].value_counts())
print(df[df["CoursePrice"] > 0][["CoursePrice","PriceBand"]].head())
print(df["PriceBand"].value_counts())

#Ab Revenue by PriceBand nikalte hain
print(df.groupby('PriceBand')['Amount'].sum())

# Most revenue is generated from medium-priced courses, 
# while free courses drive high user engagement but contribute no revenue.
#  High-priced courses also generate significant revenue despite lower enrollment,
# indicating strong premium demand.

# Duration band banate hain
def duration_band(d):
    if d < 10:
        return "short"
    elif d < 30 :
        return "medium"
    else:
        return "high"

df["DurationBand"] = df['CourseDuration'].apply(duration_band)

print(df['DurationBand'].value_counts()) 

# Longer duration courses are more popular among users, 
# indicating that learners prefer in-depth content over shorter courses.

print(df.groupby('DurationBand')['Amount'].sum())

# Medium duration courses generate the highest revenue, followed closely by long duration courses, 
# while short courses contribute the least revenue. 
# This suggests that users prefer courses with balanced depth and time commitment.

def rating_band(r):
    if r < 2:
        return "low"
    elif r < 4:
        return "medium"
    else:
        return "high"

df["RatingBand"] = df["CourseRating"].apply(rating_band)

print(df["RatingBand"].value_counts())

print(df.groupby("RatingBand")["Amount"].sum())

# Medium-rated courses generate the highest revenue, 
# while high-rated courses do not necessarily bring the most earnings. 
# This suggests that popularity and pricing may have a 
# stronger impact on revenue than ratings alone.