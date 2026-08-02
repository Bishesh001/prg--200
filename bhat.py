"""
Bhatbhateni Sales - Data Cleaning, EDA, and Insights
=====================================================
Author: Bishesh
Dataset: bhatbhateni_sales.csv (18,812 rows x 11 columns)

This is the SAME script as before, but every line now has a comment
explaining WHY it exists, not just what it does. Read this top to
bottom like a walkthrough, not just a reference.
"""

# ---------------------------------------------------------------
# IMPORTS -- every library here earns its place, nothing is random
# ---------------------------------------------------------------
import pandas as pd           # pandas is the actual engine for this whole project:
                                # it loads the CSV into a DataFrame (basically a table)
                           # and gives us groupby(), fillna(), drop_duplicates() etc.
import numpy as np             # numpy is pandas' math backbone. We don't call it much
                                # directly here, but pandas uses it under the hood, and
                                # it's standard practice to import it alongside pandas.

import matplotlib               # matplotlib is the plotting library that actually draws
                                 # the charts (bar charts, line charts, etc.)
matplotlib.use("Agg")           # This tells matplotlib "don't try to open a GUI window
                                 # to show the chart" -- because this script runs in a
                                 # terminal/container with no screen. "Agg" means: just
                                 # render the chart straight to an image file instead.
import matplotlib.pyplot as plt # pyplot is the actual drawing interface (plt.plot,
                                 # plt.bar, plt.savefig...) -- this is what you'll type
                                 # constantly whenever you make a chart.
import seaborn as sns           # seaborn sits on top of matplotlib and makes nicer-
                                 # looking charts with less code (e.g. sns.histplot,
                                 # sns.heatmap). Used here for the distribution plot,
                                 # correlation heatmap, and outlier boxplot.

from sklearn.linear_model import LinearRegression       # the actual regression model
                                                          # used in Step 16 to predict
                                                          # TotalAmount.
from sklearn.model_selection import train_test_split     # splits the data into a
                                                          # "training" chunk (model
                                                          # learns from this) and a
                                                          # "test" chunk (model is
                                                          # graded on this, data it
                                                          # never saw during training).
from sklearn.metrics import r2_score, mean_absolute_error  # these measure HOW GOOD
                                                          # the model's predictions are.
                                                          # r2_score: % of the variation
                                                          # in TotalAmount the model
                                                          # explains. mean_absolute_error:
                                                          # on average, how far off (in
                                                          # NPR) each prediction is.
from sklearn.preprocessing import OneHotEncoder          # Branch and ProductCategory are
                                                          # text (e.g. "Kathmandu - New
                                                          # Road"), but a regression model
                                                          # only understands numbers. This
                                                          # converts each text category
                                                          # into a set of 0/1 columns so
                                                          # the model can use it.
from sklearn.compose import ColumnTransformer             # lets us say "apply OneHotEncoder
                                                          # ONLY to these specific columns
                                                          # (Branch, ProductCategory), leave
                                                          # the numeric columns (Quantity,
                                                          # UnitPrice) untouched."
from sklearn.pipeline import Pipeline                     # chains "transform the data" and
                                                          # "fit the model" into a single
                                                          # object, so we can call
                                                          # .fit()/.predict() once instead
                                                          # of doing each step by hand
                                                          # every time.

import os   # only used for one thing here: os.makedirs(), to create the "outputs"
            # folder if it doesn't already exist, so plt.savefig() doesn't crash
            # trying to write into a folder that isn't there.

# ---------------------------------------------------------------
# BASIC SETUP -- small housekeeping lines that make everything below nicer
# ---------------------------------------------------------------
OUT = "outputs"                     # storing the folder name in a variable once, so if
                                     # I ever want to rename the output folder, I change
                                     # it in ONE place instead of everywhere in the file.
os.makedirs(OUT, exist_ok=True)     # create the "outputs" folder. exist_ok=True means
                                     # "don't throw an error if it already exists" -- so
                                     # this script is safe to re-run multiple times.
sns.set_style("whitegrid")          # a seaborn setting that adds light grid lines to
                                     # every chart -- purely cosmetic, makes charts
                                     # easier to read values off of.
plt.rcParams["figure.figsize"] = (9, 5)   # sets the DEFAULT size (width, height in
                                     # inches) for every chart in this script, so I
                                     # don't have to repeat figsize=(9,5) on every
                                     # single plt.figure() call.

pd.set_option("display.width", 120)       # tells pandas "when printing a DataFrame to
                                     # the terminal, use up to 120 characters per line"
                                     # so wide tables don't get ugly-wrapped.
pd.set_option("display.max_columns", 20)  # tells pandas "show up to 20 columns before
                                     # truncating with '...'" -- otherwise wide tables
                                     # get cut off and hide data you need to see.


# =====================================================================
# STEP 1-2: LOAD LIBRARIES & DATA
# =====================================================================
# Libraries: pandas/numpy for wrangling, matplotlib/seaborn for plots,
# scikit-learn for the regression model in Step 16.

df = pd.read_csv(r"C:\Users\NIC\Downloads\bhatbhateni_sales_cleaned.csv")
# This is the single most important line in the whole script -- it reads the CSV
# file off disk and loads it into "df" (short for DataFrame, pandas' name for a
# table). Every single line after this works on "df". Note the path: the script
# expects a folder called "data" sitting right next to this .py file, with the
# CSV inside it -- that's why you need that folder structure to run this.

# =====================================================================
# STEP 3: INSPECT
# =====================================================================
print("=" * 70)              # just prints a line of 70 "=" characters, purely to make
print("STEP 3: INITIAL INSPECTION")   # the terminal output visually split into sections,
print("=" * 70)               # so it's easier to scroll through and find a step.

print("\nQ3a. First 5 rows:")
print(df.head())
# df.head() shows the first 5 rows by default. This answers Q3a directly and is
# also just good habit -- ALWAYS look at your raw data before doing anything to
# it, so you know what you're actually working with.

print(f"\nQ3b. Shape: {df.shape[0]} rows, {df.shape[1]} columns")
# df.shape returns a pair like (18812, 11) -- (number of rows, number of columns).
# shape[0] pulls out the row count, shape[1] the column count. This directly
# answers "how many rows and columns does the dataset have?"

print(f"\nQ3c. Columns: {list(df.columns)}")
# df.columns gives the column names. Wrapping it in list() just makes it print
# as a clean Python list instead of pandas' slightly noisier Index object format.

# =====================================================================
# STEP 4: DATA TYPES & STRUCTURE
# =====================================================================
print("\n" + "=" * 70)
print("STEP 4: DATA TYPES")
print("=" * 70)
print("\nQ4a. Dtypes:")
print(df.dtypes)
# df.dtypes shows what TYPE of data pandas thinks is in each column (text, whole
# number, decimal number, etc). This matters because you can't do math on text,
# and Date needs to become a real date type before we can do anything time-based
# with it (that fix happens later, in Step 8a).

# Date is loaded as object/string -> needs conversion to datetime (Step 8a).
# Everything else's dtype already matches its meaning: IDs/names/categoricals
# as strings, Quantity as int, UnitPrice/TotalAmount as float.

print("\nQ4b. Summary statistics (numeric columns):")
print(df.describe())
# df.describe() automatically finds every NUMERIC column and gives you count,
# mean, std (how spread out the values are), min, 25%/50%/75% (quartiles), and
# max -- all in one call. This is the fastest way to get a "feel" for a numeric
# column before you plot anything.

# Quantity ranges 1-4 (small basket sizes, capped design). UnitPrice and
# TotalAmount are right-skewed (mean > median), consistent with a retail
# mix of cheap groceries and a few expensive electronics/apparel items.

# =====================================================================
# STEP 5: DETECT DATA QUALITY ISSUES
# =====================================================================
print("\n" + "=" * 70)
print("STEP 5: DATA QUALITY ISSUES")
print("=" * 70)

print("\nQ5a. Missing values (count and %):")
null_summary = pd.DataFrame({
    "missing_count": df.isnull().sum(),
    # df.isnull() turns the WHOLE table into True/False (True = missing value).
    # .sum() on that then counts the True's per column (True counts as 1, False
    # as 0) -- so this line gives "how many missing values in each column".
    "missing_pct": (df.isnull().sum() / len(df) * 100).round(2)
    # same missing count, but divided by len(df) (total row count) and x100 to
    # turn it into a percentage, then .round(2) to keep it readable (2 decimal
    # places instead of a long decimal).
})
null_summary = null_summary[null_summary["missing_count"] > 0].sort_values(
    "missing_count", ascending=False
)
# this line does two things: (1) filters OUT any column that has 0 missing
# values, so we only see the columns that actually have a problem, and (2)
# sorts what's left so the worst offender (most missing values) shows up first.
print(null_summary)
# Affected: PaymentMethod (468, 2.49%), CustomerName (568, 3.02%),
# UnitPrice (371, 1.97%), ProductCategory (282, 1.50%)

print("\nQ5b. Fully duplicated rows:")
full_dupes = df.duplicated().sum()
# df.duplicated() checks EVERY column at once and marks a row True if it's an
# exact copy of an earlier row (all 11 columns identical). .sum() counts how
# many True's -- so this is "how many fully duplicated rows exist."
print(f"{full_dupes} exact duplicate rows")

print("\nQ5c. TransactionID repeats vs. true duplicates:")
txn_repeats = df["TransactionID"].duplicated().sum()
# This is different from the line above -- here we only check ONE column
# (TransactionID). A "repeat" here just means the SAME TransactionID appears
# more than once, which is expected (one shopping trip = multiple product rows
# under the same TransactionID). It doesn't mean the whole row is duplicated.
print(f"{txn_repeats} rows share a TransactionID with another row.")
print("A repeat TransactionID is a genuine multi-item basket if the OTHER")
print("columns differ (different ProductName/Quantity/etc). It's a TRUE")
print("duplicate only if every column matches. Check:")
same_txn_diff_product = df.duplicated(subset=["TransactionID"], keep=False) & \
                         ~df.duplicated(keep=False)
# This is the trickiest line in the whole script, so slow down here:
#   - df.duplicated(subset=["TransactionID"], keep=False) marks EVERY row that
#     shares its TransactionID with at least one other row (keep=False means
#     "mark ALL of them, not just the 2nd/3rd copy").
#   - df.duplicated(keep=False) (no subset) marks EVERY row that is a FULL
#     duplicate of another row (checking all columns), again marking all copies.
#   - The "~" in front of the second one means NOT -- so "~df.duplicated(...)"
#     means "rows that are NOT full duplicates."
#   - The "&" combines both conditions with AND: "shares a TransactionID" AND
#     "is NOT a full duplicate" = a legitimate repeat line-item (same basket,
#     different product), not a copy-paste error.
print(f"  -> {same_txn_diff_product.sum()} rows are legitimate repeat "
      f"line-items (same TransactionID, different product/details)")
print(f"  -> {full_dupes} rows are true full-row duplicates (handled in Step 6)")

print("\nQ5d. Illogical values (TotalAmount != Quantity * UnitPrice):")
check = df.dropna(subset=["UnitPrice"]).copy()
# We can only check this math for rows that actually HAVE a UnitPrice (some are
# missing at this point, that gets fixed later in Step 7c). dropna(subset=...)
# temporarily drops rows missing UnitPrice, just for this check. .copy() makes
# an independent copy so pandas doesn't complain about editing a "slice" of df.
check["calc_amount"] = (check["Quantity"] * check["UnitPrice"]).round(2)
# manually recompute what TotalAmount SHOULD be, using the formula that should
# hold true: Quantity x UnitPrice. round(2) keeps it to 2 decimal places (money
# doesn't need more precision than cents/paisa).
mismatches = check[(check["calc_amount"] - check["TotalAmount"]).abs() > 0.01]
# subtract our recalculated amount from the actual TotalAmount column, take the
# absolute value (so it doesn't matter if it's off by +5 or -5), and keep only
# rows where that difference is bigger than 1 paisa (0.01) -- i.e. rows where
# the math doesn't add up.
print(f"{len(mismatches)} rows where TotalAmount doesn't match Quantity*UnitPrice")
# 0 mismatches found among rows with a known UnitPrice -> the data is
# internally consistent, which is exactly why we can *reverse-engineer*
# missing UnitPrice values from TotalAmount / Quantity in Step 7c.

# =====================================================================
# STEP 6: HANDLE DUPLICATE ROWS
# =====================================================================
print("\n" + "=" * 70)
print("STEP 6: REMOVE DUPLICATE ROWS")
print("=" * 70)

rows_before = len(df)
# len(df) gives the row count. We save it BEFORE removing anything, so we can
# compare "before" vs "after" and prove the cleanup actually did something
# reasonable (not too much, not too little).
df = df.drop_duplicates(keep="first").reset_index(drop=True)
# drop_duplicates() removes rows that are FULL duplicates (every column
# matches another row). keep="first" means "when there are copies, keep the
# first one you find and delete the rest" -- so we don't lose the data
# entirely, just the extra copies. reset_index(drop=True) renumbers the rows
# 0,1,2,3... afterward -- without this, the row numbers would have gaps where
# duplicates used to be, which looks messy and can cause bugs later.
rows_after = len(df)
# row count again, AFTER the cleanup, so we can report the difference.

print(f"Q6a/Q6b. Rows before: {rows_before}, after: {rows_after}, "
      f"removed: {rows_before - rows_after}")
assert df.duplicated().sum() == 0, "Duplicates still present!"
# assert is a safety check: "I BELIEVE this is now True -- if it's not, stop
# the whole script and show me this error message." Here it's confirming that
# after drop_duplicates(), running the same duplicate check again gives 0.
# This isn't just decoration -- if this line ever fails, it means something
# is wrong with the cleaning logic, and I want the script to crash loudly
# rather than silently continue with bad data.
print("Verified: 0 duplicate rows remain.")

# =====================================================================
# STEP 7: HANDLE MISSING VALUES
# =====================================================================
print("\n" + "=" * 70)
print("STEP 7: HANDLE MISSING VALUES")
print("=" * 70)

# --- Q7a: CustomerName -------------------------------------------------
# CustomerName is an identity field tied 1:1 to CustomerID (every CustomerID
# maps to exactly one name in the non-null rows), so we recover it from
# CustomerID wherever possible instead of guessing or dropping rows.
cust_lookup = (
    df.dropna(subset=["CustomerName"])
      # first, throw away rows where CustomerName is ALSO missing -- we can't
      # use a missing name to fill in another missing name.
      .drop_duplicates("CustomerID")
      # each CustomerID should map to exactly one name, so if the same
      # CustomerID appears many times (many purchases), we only need ONE of
      # those rows to know their name -- drop_duplicates("CustomerID") keeps
      # just the first occurrence of each ID.
      .set_index("CustomerID")["CustomerName"]
      # turns this into a lookup table: set_index("CustomerID") makes
      # CustomerID the "key" you search by, and ["CustomerName"] pulls out just
      # the name column -- so now cust_lookup["CUST1005"] would instantly give
      # you that customer's name.
)
missing_name_before = df["CustomerName"].isnull().sum()
# count how many names are missing BEFORE we try to fix anything, so we can
# report how many we actually managed to recover.
df["CustomerName"] = df["CustomerName"].fillna(df["CustomerID"].map(cust_lookup))
# .map(cust_lookup) looks up each row's CustomerID in our lookup table and
# returns the matching name (or nothing, if that ID has no known name at all).
# .fillna(...) then says "wherever CustomerName is currently empty, use this
# looked-up value instead" -- rows that already had a name are left untouched.
still_missing_name = df["CustomerName"].isnull().sum()
# after the fillna above, check again how many are STILL missing -- these are
# customers whose name was never recorded anywhere in the whole dataset, so
# there was nothing to look up.
df["CustomerName"] = df["CustomerName"].fillna("Unknown Customer")
# for the handful that are still missing, we can't recover them, so instead of
# leaving a blank (which would break later groupby/analysis steps), we
# explicitly label them "Unknown Customer" -- honest and easy to filter later
# if needed.
print(f"Q7a. CustomerName: {missing_name_before} missing -> "
      f"{missing_name_before - still_missing_name} recovered via CustomerID, "
      f"{still_missing_name} left as 'Unknown Customer' (no other record for that ID)")

# --- Q7b: ProductCategory ----------------------------------------------
# ProductCategory is fully determined by ProductName in this dataset
# (each product belongs to exactly one category), so we build a
# ProductName -> ProductCategory lookup and fill from it.
cat_lookup = (
    df.dropna(subset=["ProductCategory"])
      .drop_duplicates("ProductName")
      .set_index("ProductName")["ProductCategory"]
)
# exact same idea as cust_lookup above, just for products instead of
# customers: "Wall Clock" always belongs to "Household", so we build a
# ProductName -> ProductCategory dictionary from the rows where we DO know
# the category, then use it to fill in the ones we don't.
missing_cat_before = df["ProductCategory"].isnull().sum()
df["ProductCategory"] = df["ProductCategory"].fillna(df["ProductName"].map(cat_lookup))
print(f"Q7b. ProductCategory: {missing_cat_before} missing -> "
      f"{df['ProductCategory'].isnull().sum()} remaining after mapping from ProductName")

# --- Q7c: UnitPrice ------------------------------------------------------
# Since Step 5d proved TotalAmount == Quantity * UnitPrice everywhere it's
# known, the exact recovery is UnitPrice = TotalAmount / Quantity. This is
# more accurate than a category median because it reconstructs the *actual*
# original value rather than an estimate.
missing_price_before = df["UnitPrice"].isnull().sum()
recovered_price = (df["TotalAmount"] / df["Quantity"]).round(2)
# this is just rearranging the formula we already trust: if
# TotalAmount = Quantity x UnitPrice, then UnitPrice = TotalAmount / Quantity.
# We calculate this for EVERY row (even ones that aren't missing UnitPrice),
# but that's fine -- the next line only actually USES it where needed.
df["UnitPrice"] = df["UnitPrice"].fillna(recovered_price)
# fillna again: wherever UnitPrice is empty, plug in the value we just
# calculated. Rows that already had a UnitPrice keep their original value.
print(f"Q7c. UnitPrice: {missing_price_before} missing -> "
      f"{df['UnitPrice'].isnull().sum()} remaining "
      f"(all recovered exactly via TotalAmount / Quantity)")

# --- Q7d: PaymentMethod --------------------------------------------------
# PaymentMethod has no reliable predictor column in this dataset (it's not
# derivable from Branch, ProductCategory, etc. with any confidence), and
# imputing a payment method (e.g. filling with the mode "Cash") would
# quietly distort the digital-vs-cash payment mix analysis in Step 14.
# Flagging as "Unknown" preserves the missingness as real information
# instead of inventing a fact.
missing_pay_before = df["PaymentMethod"].isnull().sum()
df["PaymentMethod"] = df["PaymentMethod"].fillna("Unknown")
# unlike the columns above, there's NOTHING else in the row that tells us what
# payment method someone used -- so instead of guessing (which would quietly
# lie in the analysis), we just label it "Unknown" and keep it honest.
print(f"Q7d. PaymentMethod: {missing_pay_before} missing -> filled with "
      f"'Unknown' (not imputed/dropped) to avoid distorting payment-mix analysis")

# --- Q7e: confirm no missing values --------------------------------------
print("\nQ7e. Final missing-value check:")
print(df.isnull().sum())
# run the exact same missing-value check from Step 5a, one more time, so we
# can visually confirm every column now shows 0.
assert df.isnull().sum().sum() == 0, "Still have nulls!"
# double .sum() here: the first .sum() gives missing-count PER COLUMN (like
# before), the second .sum() adds THOSE numbers together into one single
# total. If that grand total isn't exactly 0, this line stops the script and
# tells us cleaning isn't actually finished -- another safety net, same idea
# as the duplicate-check assert in Step 6.
print("Confirmed: 0 missing values across all columns.")

# =====================================================================
# STEP 8: CLEANING & FEATURE ENGINEERING
# =====================================================================
print("\n" + "=" * 70)
print("STEP 8: FEATURE ENGINEERING")
print("=" * 70)

# Q8a: Date -> datetime + time features
df["Date"] = pd.to_datetime(df["Date"])
# right now, Date is just TEXT that happens to look like "2025-05-19" -- pandas
# has no idea it's actually a date. pd.to_datetime() converts it into a real
# datetime type, which unlocks things like .dt.month, .dt.day_name(), sorting
# chronologically, and date math -- none of which work on plain text.
df["Year"] = df["Date"].dt.year          # pulls just the year (2025) into its own column
df["Month"] = df["Date"].dt.month        # pulls the month as a NUMBER (1-12) -- useful
                                          # for sorting months in calendar order later
df["MonthName"] = df["Date"].dt.month_name()  # pulls the month as TEXT ("January") --
                                          # useful for readable chart labels
df["DayOfWeek"] = df["Date"].dt.day_name()    # pulls the day name ("Monday", "Tuesday"...)
df["IsWeekend"] = df["Date"].dt.dayofweek >= 5
# .dt.dayofweek gives a number: Monday=0, Tuesday=1, ... Saturday=5, Sunday=6.
# ">= 5" checks if that number is 5 or 6, which is exactly Saturday or Sunday
# -- so this line creates a True/False column for "was this a weekend sale?"
print("Q8a. Date converted to datetime; added Year, Month, MonthName, "
      "DayOfWeek, IsWeekend")

# Q8b: Branch -> City
# Branch is formatted "City - Area", so split on " - " and keep the city part.
df["City"] = df["Branch"].str.split(" - ").str[0]
# .str.split(" - ") breaks a string like "Kathmandu - New Road" into a list:
# ["Kathmandu", "New Road"]. .str[0] then grabs just the FIRST item in that
# list for every row -- i.e. the city name, throwing away the area/neighborhood
# part. This lets us group sales by city later (Step 11c) without a city
# appearing multiple times under slightly different branch names.
print(f"Q8b. City extracted from Branch. Cities: {sorted(df['City'].unique())}")
# df['City'].unique() lists every distinct city with no repeats, sorted()
# puts them in alphabetical order just for a clean printout.

# Q8c: Recompute/validate TotalAmount after fixing UnitPrice
df["TotalAmount_check"] = (df["Quantity"] * df["UnitPrice"]).round(2)
# same idea as Step 5d's "check" column, but now run AFTER we fixed the
# missing UnitPrice values -- this proves the fix in Step 7c actually worked
# and didn't accidentally break the Quantity x UnitPrice = TotalAmount rule.
mismatch_after = (df["TotalAmount_check"] - df["TotalAmount"]).abs() > 0.01
print(f"Q8c. Rows where TotalAmount disagrees with Quantity*UnitPrice after "
      f"cleaning: {mismatch_after.sum()} (0 expected, since UnitPrice was "
      f"reverse-engineered from TotalAmount itself)")
df = df.drop(columns=["TotalAmount_check"])
# we only needed that column temporarily to run the check above -- now that
# we've confirmed it matches, we drop it so it doesn't clutter the final
# cleaned dataset with a redundant column.

df.to_csv(f"{OUT}/bhatbhateni_sales_cleaned.csv", index=False)
# save the fully cleaned DataFrame to a new CSV file, so anyone (including
# future-me) can open the CLEANED version directly without re-running the
# whole script. index=False stops pandas from adding its own row-number
# column (0,1,2...) into the saved file -- we don't need it, it's just noise.
print(f"\nCleaned dataset saved -> {OUT}/bhatbhateni_sales_cleaned.csv")

# =====================================================================
# STEP 9: UNIVARIATE ANALYSIS
# =====================================================================
# "Univariate" just means "looking at ONE variable/column at a time" -- as
# opposed to later steps where we compare TWO things against each other
# (like revenue x branch, or revenue x time).
print("\n" + "=" * 70)
print("STEP 9: UNIVARIATE ANALYSIS")
print("=" * 70)

print("\nQ9a. Transactions by ProductCategory:")
print(df["ProductCategory"].value_counts())
# value_counts() is one of the most useful pandas functions there is: it
# counts how many times each unique value appears in a column, automatically
# sorted from most common to least common. Here: how many transactions fall
# into each category.

plt.figure()                       # start a brand-new blank chart (so this plot
                                    # doesn't get drawn on top of a previous one)
df["ProductCategory"].value_counts().plot(kind="bar", color="#2E86AB")
# takes the value_counts() result from above and turns it straight into a bar
# chart -- pandas Series objects have a built-in .plot() method, so we don't
# need to manually feed x/y values into matplotlib.
plt.title("Transactions by Product Category")   # chart title
plt.ylabel("Number of Transactions")             # label for the vertical axis
plt.xlabel("Product Category")                   # label for the horizontal axis
plt.tight_layout()                 # auto-adjusts spacing so labels don't get cut
                                    # off at the edges of the image -- almost
                                    # always worth adding before saving a chart
plt.savefig(f"{OUT}/09a_category_distribution.png", dpi=150)
# saves the chart as a PNG image file instead of trying to "show" it on
# screen (remember, we set matplotlib to "Agg" mode earlier, no screen
# available). dpi=150 controls image sharpness/resolution -- higher dpi =
# crisper image but bigger file size.
plt.close()                        # closes this chart so it doesn't stay in
                                    # memory or accidentally get drawn on by the
                                    # NEXT plt.figure() call below.

print("\nQ9b. Transactions by Branch:")
print(df["Branch"].value_counts())

plt.figure()
df["Branch"].value_counts().plot(kind="barh", color="#A23B72")
# kind="barh" instead of "bar" -- the "h" makes it a HORIZONTAL bar chart
# instead of vertical. Branch names are long text, so horizontal bars keep
# the labels readable instead of squishing/rotating them.
plt.title("Transactions by Branch")
plt.xlabel("Number of Transactions")
plt.tight_layout()
plt.savefig(f"{OUT}/09b_branch_distribution.png", dpi=150)
plt.close()

print("\nQ9c. Most common PaymentMethod:")
print(df["PaymentMethod"].value_counts())
print(f"-> Most common: {df['PaymentMethod'].value_counts().idxmax()}")
# .idxmax() finds the "index" (the category label) that has the MAXIMUM
# value -- since value_counts() is already sorted biggest-first, this is
# just grabbing the very first/top label, i.e. whichever payment method was
# used the most.

print(f"\nQ9d. TotalAmount distribution: mean={df['TotalAmount'].mean():.2f}, "
      f"median={df['TotalAmount'].median():.2f}, skew={df['TotalAmount'].skew():.2f}")
# mean = simple average. median = the "middle" value if you lined up every
# transaction from smallest to largest. skew = a single number describing
# lopsidedness: 0 means perfectly symmetric, positive means a long tail
# stretching toward BIGGER values (a few huge purchases pulling the average
# up), negative means the opposite. ":.2f" just formats each number to 2
# decimal places so the printout isn't a huge string of digits.
print("Mean well above median and positive skew -> right-skewed distribution "
      "(a long tail of high-value transactions, mostly Electronics/Apparel).")

plt.figure()
sns.histplot(df["TotalAmount"], bins=50, kde=True, color="#F18F01")
# histplot draws a histogram: it buckets TotalAmount values into 50 "bins"
# (bins=50) and shows how many transactions fall into each bucket as bars.
# kde=True overlays a smooth curve on top showing the estimated shape of the
# distribution -- makes the skew visually obvious.
plt.title("Distribution of TotalAmount (right-skewed)")
plt.xlabel("Total Amount (NPR)")
plt.tight_layout()
plt.savefig(f"{OUT}/09d_totalamount_distribution.png", dpi=150)
plt.close()

# =====================================================================
# STEP 10: SALES TREND ANALYSIS
# =====================================================================
print("\n" + "=" * 70)
print("STEP 10: SALES TREND ANALYSIS")
print("=" * 70)

print("\nQ10a. Monthly revenue trend (2025):")
monthly = df.groupby(["Month", "MonthName"])["TotalAmount"].sum().reset_index()
# groupby(["Month", "MonthName"]) buckets every row by which month it happened
# in (using BOTH the number and the name together, so we get one row per
# actual month, not a weird mix). ["TotalAmount"].sum() then adds up all the
# revenue within each of those monthly buckets. .reset_index() turns the
# result back into a normal flat table (by default, groupby results use the
# group labels as a special index instead of a regular column, which is
# awkward to plot -- reset_index() undoes that).
monthly = monthly.sort_values("Month")
# groupby doesn't guarantee calendar order (it might sort alphabetically by
# MonthName instead, e.g. "April" before "January"), so we explicitly
# re-sort by the numeric Month column to get Jan->Dec order for the chart.
print(monthly)

plt.figure()
plt.plot(monthly["MonthName"], monthly["TotalAmount"], marker="o", color="#2E86AB")
# plt.plot() draws a LINE chart -- ideal for showing a trend over time (as
# opposed to bar charts, which are better for comparing separate categories).
# marker="o" adds a visible dot at each actual data point on the line, so you
# can see exactly where each month's value sits.
plt.title("Monthly Revenue Trend — 2025")
plt.ylabel("Revenue (NPR)")
plt.xticks(rotation=45)
# rotates the month name labels 45 degrees on the x-axis -- without this,
# 12 month names side-by-side would overlap and be unreadable.
plt.tight_layout()
plt.savefig(f"{OUT}/10a_monthly_revenue_trend.png", dpi=150)
plt.close()

print("\nQ10b. Weekend vs weekday revenue:")
weekend_rev = df.groupby("IsWeekend")["TotalAmount"].agg(["sum", "mean", "count"])
# groupby("IsWeekend") splits the data into exactly 2 buckets: True (weekend)
# and False (weekday). .agg(["sum","mean","count"]) then calculates THREE
# different statistics for each bucket in one go: total revenue (sum),
# average transaction size (mean), and how many transactions happened
# (count) -- instead of writing three separate lines for each stat.
weekend_rev.index = weekend_rev.index.map({True: "Weekend", False: "Weekday"})
# by default the row labels would just say "True"/"False", which is
# technically correct but not very readable in a printed report -- this line
# renames them to actual words.
print(weekend_rev)

print("\nQ10c. Revenue by day of week:")
dow_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# groupby would normally sort day names ALPHABETICALLY (Friday, Monday,
# Saturday...), which makes no sense for a day-of-week chart. So we manually
# define the correct calendar order here, to reorder the results with next.
dow_rev = df.groupby("DayOfWeek")["TotalAmount"].sum().reindex(dow_order)
# groupby+sum gives total revenue per day name (in the wrong, alphabetical
# order). .reindex(dow_order) then re-arranges those same rows to follow our
# dow_order list instead -- Monday through Sunday, like a normal calendar.
print(dow_rev)
print(f"-> Highest revenue day: {dow_rev.idxmax()}")
# same idxmax() trick as before -- find which day label has the single
# largest revenue value.

plt.figure()
dow_rev.plot(kind="bar", color="#C73E1D")
plt.title("Revenue by Day of Week")
plt.ylabel("Revenue (NPR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{OUT}/10c_revenue_by_dayofweek.png", dpi=150)
plt.close()

# =====================================================================
# STEP 11: BRANCH & CITY PERFORMANCE
# =====================================================================
print("\n" + "=" * 70)
print("STEP 11: BRANCH & CITY PERFORMANCE")
print("=" * 70)

print("\nQ11a. Revenue by branch:")
branch_rev = df.groupby("Branch")["TotalAmount"].sum().sort_values(ascending=False)
# group all rows by Branch, sum up TotalAmount within each branch, then sort
# so the HIGHEST-revenue branch appears first (ascending=False means
# "biggest to smallest", not "smallest to biggest").
print(branch_rev)
print(f"-> Top branch: {branch_rev.idxmax()}")

print("\nQ11b. Average transaction value (basket size) by branch:")
branch_avg = df.groupby("Branch")["TotalAmount"].mean().sort_values(ascending=False)
# same grouping as above, but .mean() instead of .sum() -- this tells us the
# AVERAGE size of a single purchase at each branch, which is a different
# question than "which branch makes the most money overall" (a branch could
# have low total revenue but each customer spends a lot per visit, or vice
# versa).
print(branch_avg.round(2))

plt.figure()
branch_rev.plot(kind="barh", color="#2E86AB")
plt.title("Total Revenue by Branch")
plt.xlabel("Revenue (NPR)")
plt.tight_layout()
plt.savefig(f"{OUT}/11a_branch_revenue.png", dpi=150)
plt.close()

print("\nQ11c. Revenue by city:")
city_rev = df.groupby("City")["TotalAmount"].sum().sort_values(ascending=False)
# this only works because we built the "City" column back in Step 8b -- this
# is a good example of why feature engineering earlier pays off later:
# without a City column, we couldn't ask "which CITY makes the most money"
# directly, only "which branch."
print(city_rev)
print(f"-> Top city: {city_rev.idxmax()}")

# =====================================================================
# STEP 12: PRODUCT CATEGORY & PRODUCT ANALYSIS
# =====================================================================
print("\n" + "=" * 70)
print("STEP 12: PRODUCT ANALYSIS")
print("=" * 70)

print("\nQ12a. Revenue vs transaction count by category:")
cat_summary = df.groupby("ProductCategory").agg(
    Revenue=("TotalAmount", "sum"),
    # this "named aggregation" syntax means: create a new column called
    # "Revenue" by summing the TotalAmount column within each category group.
    Transactions=("TransactionID", "count")
    # and create a column called "Transactions" by COUNTING how many
    # TransactionID entries fall into each category group. Using .agg() with
    # names like this (instead of two separate groupby lines) keeps both
    # results neatly side-by-side in one table.
).sort_values("Revenue", ascending=False)
print(cat_summary)
# This table is genuinely useful because it lets you compare two DIFFERENT
# questions side by side: "which category makes the most MONEY" vs "which
# category is bought the most OFTEN" -- and those are not always the same
# category (a category can have few but expensive sales, or many but cheap
# ones).

plt.figure()
cat_summary["Revenue"].plot(kind="bar", color="#A23B72")
plt.title("Revenue by Product Category")
plt.ylabel("Revenue (NPR)")
plt.tight_layout()
plt.savefig(f"{OUT}/12a_category_revenue.png", dpi=150)
plt.close()

print("\nQ12b. Top 10 products by quantity sold:")
top_qty = df.groupby("ProductName")["Quantity"].sum().sort_values(ascending=False).head(10)
# group by individual product (not category this time), sum up how many
# UNITS were sold of each one, sort biggest-first, then .head(10) keeps only
# the top 10 rows -- gives us a "bestsellers by volume" list.
print(top_qty)

print("\nQ12c. Top 10 products by revenue:")
top_rev = df.groupby("ProductName")["TotalAmount"].sum().sort_values(ascending=False).head(10)
# same idea, but summing TotalAmount instead of Quantity -- "bestsellers by
# money brought in", which can be a totally different list (a product can
# sell a LOT of cheap units, or a FEW expensive ones, and both can rank
# highly here for different reasons).
print(top_rev)

# =====================================================================
# STEP 13: CUSTOMER ANALYSIS
# =====================================================================
print("\n" + "=" * 70)
print("STEP 13: CUSTOMER ANALYSIS")
print("=" * 70)

print("\nQ13a. Top 10 customers by spend:")
top_customers = df.groupby(["CustomerID", "CustomerName"])["TotalAmount"].sum() \
                  .sort_values(ascending=False).head(10)
# grouping by BOTH CustomerID and CustomerName together (instead of just
# CustomerID) means the printed result shows the actual name next to the ID,
# which is much more readable than a list of anonymous customer codes.
print(top_customers)

print("\nQ13b. Repeat vs one-time customers:")
txn_per_customer = df.groupby("CustomerID")["TransactionID"].nunique()
# .nunique() counts how many DISTINCT (unique) TransactionIDs each customer
# has -- i.e. how many separate shopping trips they made (not how many
# product rows, since one trip can have several product rows).
repeat = (txn_per_customer > 1).sum()
# txn_per_customer > 1 turns the count into True/False per customer (True =
# came back more than once). .sum() then adds up the True's, i.e. counts how
# many customers are repeat shoppers.
one_time = (txn_per_customer == 1).sum()
# same idea, but for customers with EXACTLY 1 visit -- one-time shoppers.
print(f"Repeat customers: {repeat}, One-time customers: {one_time}")

print("\nQ13c. Average spend per customer (CLV proxy):")
clv = df.groupby("CustomerID")["TotalAmount"].sum()
# CLV = "Customer Lifetime Value" -- here it's approximated (a "proxy", not
# a textbook CLV formula) as simply: total amount that customer has spent
# across all their transactions in this dataset.
print(f"Average customer lifetime spend: NPR {clv.mean():.2f}")
print(f"Median customer lifetime spend: NPR {clv.median():.2f}")
# printing both mean AND median here on purpose -- if they're far apart (like
# they are), it tells us customer spending is skewed too, just like
# TotalAmount was in Q9d: a few big spenders pull the average up above what a
# "typical" customer actually spends.

# =====================================================================
# STEP 14: PAYMENT METHOD ANALYSIS
# =====================================================================
print("\n" + "=" * 70)
print("STEP 14: PAYMENT METHOD ANALYSIS")
print("=" * 70)

print("\nQ14a. Payment method mix by branch (% of transactions):")
pay_branch = pd.crosstab(df["Branch"], df["PaymentMethod"], normalize="index") * 100
# pd.crosstab() builds a table counting how often every combination of
# Branch and PaymentMethod occurs together -- branches as rows, payment
# methods as columns. normalize="index" converts those raw counts into
# PERCENTAGES of each row (so each branch's row adds up to 100%), which
# makes it possible to fairly compare a big branch against a small one.
# x 100 just converts the 0-1 decimal into an actual percentage number.
print(pay_branch.round(1))

print("\nQ14b. Average transaction value by payment method:")
pay_avg = df.groupby("PaymentMethod")["TotalAmount"].mean().sort_values(ascending=False)
print(pay_avg.round(2))

plt.figure()
pay_avg.plot(kind="bar", color="#F18F01")
plt.title("Average Transaction Value by Payment Method")
plt.ylabel("Average Amount (NPR)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(f"{OUT}/14b_avg_by_payment.png", dpi=150)
plt.close()

# =====================================================================
# STEP 15: CORRELATION & OUTLIERS
# =====================================================================
print("\n" + "=" * 70)
print("STEP 15: CORRELATION & OUTLIER DETECTION")
print("=" * 70)

print("\nQ15a. Correlation matrix (Quantity, UnitPrice, TotalAmount):")
corr = df[["Quantity", "UnitPrice", "TotalAmount"]].corr()
# .corr() calculates the correlation coefficient between every PAIR of the
# selected numeric columns, all at once. A correlation close to +1 means
# "when one goes up, the other goes up too, strongly". Close to 0 means "no
# real relationship". Close to -1 means "when one goes up, the other goes
# down". The result is a small grid (3x3 here, since we picked 3 columns)
# showing every column compared against every other column.
print(corr.round(3))
print("UnitPrice correlates strongly with TotalAmount (price drives revenue "
      "per transaction more than basket quantity does, since Quantity is "
      "capped at 1-4).")

plt.figure()
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0)
# heatmap turns that correlation grid into a color-coded picture -- easier
# to scan at a glance than raw numbers. annot=True prints the actual number
# inside each colored square. cmap="coolwarm" picks a color scheme where
# one end is "cool" (blue, for negative correlation) and the other is "warm"
# (red, for positive). center=0 makes sure 0 correlation lands exactly on
# the neutral color in the middle of that scheme, so the colors are
# meaningful and not skewed.
plt.title("Correlation: Quantity, UnitPrice, TotalAmount")
plt.tight_layout()
plt.savefig(f"{OUT}/15a_correlation_heatmap.png", dpi=150)
plt.close()

print("\nQ15b. Outliers in TotalAmount via IQR:")
Q1 = df["TotalAmount"].quantile(0.25)
# the 25th percentile -- the value below which 25% of all transactions fall.
Q3 = df["TotalAmount"].quantile(0.75)
# the 75th percentile -- the value below which 75% of all transactions fall.
IQR = Q3 - Q1
# IQR = "Interquartile Range" -- the spread of the MIDDLE 50% of the data
# (between the 25th and 75th percentile), ignoring extreme values on both
# ends. It's a standard, well-known way to measure "typical spread" that
# isn't thrown off by outliers, unlike something like standard deviation.
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
# this "1.5 x IQR" rule is a widely-used statistical convention (not
# something I invented) for drawing outlier boundaries: anything below
# Q1 - 1.5xIQR or above Q3 + 1.5xIQR is flagged as unusually far from the
# typical range.
outliers = df[(df["TotalAmount"] < lower) | (df["TotalAmount"] > upper)]
# keep only the rows where TotalAmount falls OUTSIDE those two boundaries
# (the "|" means OR -- either too low, or too high).
print(f"IQR bounds: [{lower:.2f}, {upper:.2f}]")
print(f"Outlier transactions: {len(outliers)} ({len(outliers)/len(df)*100:.2f}% of data)")
print("These are legitimate high-value purchases (Electronics/Apparel), not "
      "data errors — Step 5d already confirmed TotalAmount = Quantity*UnitPrice "
      "holds everywhere, so they reflect real big-ticket items, not typos.")

plt.figure()
sns.boxplot(x=df["TotalAmount"], color="#2E86AB")
# a boxplot visually shows the same IQR concept as a "box" (middle 50% of
# data), with a line for the median, and individual dots plotted beyond the
# whiskers for anything flagged as an outlier -- a quick visual companion to
# the numeric outlier count above.
plt.title("TotalAmount — Outlier Detection (IQR method)")
plt.tight_layout()
plt.savefig(f"{OUT}/15b_outlier_boxplot.png", dpi=150)
plt.close()

# =====================================================================
# STEP 16: PREDICTIVE MODELING (simple linear regression)
# =====================================================================
print("\n" + "=" * 70)
print("STEP 16: PREDICTIVE MODELING")
print("=" * 70)

features = ["Quantity", "UnitPrice", "Branch", "ProductCategory"]
# these are the columns we're ALLOWED to use to predict TotalAmount -- picked
# because the assignment specifically asked for these four.
X = df[features]     # X (capital, by ML convention) = the "input" columns the
                      # model is allowed to look at.
y = df["TotalAmount"]  # y (lowercase, by convention) = the "answer" column we
                      # want the model to learn to predict.

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# splits X and y into two matching chunks: 80% for TRAINING (the model
# learns patterns from this) and 20% for TESTING (held back completely, used
# only to grade the model afterward on data it's never seen -- this is how
# you catch a model that just "memorized" the training data instead of
# actually learning a real pattern). test_size=0.2 means 20% goes to
# testing. random_state=42 just fixes the random shuffling so that if I run
# this again, I get the EXACT same split -- makes results reproducible
# instead of changing every run.

preprocess = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), ["Branch", "ProductCategory"])
        # apply OneHotEncoder ONLY to these two text columns. handle_unknown=
        # "ignore" means "if the test data somehow contains a branch/category
        # value the model never saw during training, don't crash -- just
        # treat it as all-zeros instead."
    ],
    remainder="passthrough"
    # "passthrough" means "any column NOT mentioned above (Quantity,
    # UnitPrice) should be left completely as-is, unchanged" -- they're
    # already numbers, so they don't need encoding.
)

model = Pipeline(steps=[
    ("preprocess", preprocess),
    ("regressor", LinearRegression())
])
# a Pipeline bundles "first transform the data, then feed it into the model"
# into ONE object. This matters because it guarantees the exact same
# transformation is applied automatically both when training AND when
# predicting later -- you can't accidentally forget to encode the test data
# the same way you encoded the training data.

model.fit(X_train, y_train)
# this is where the actual "learning" happens: the model looks at X_train
# and y_train together and works out the best-fitting linear relationship
# between the input features and TotalAmount.
y_pred = model.predict(X_test)
# now we ask the trained model to predict TotalAmount for the TEST set --
# data it never saw during .fit() -- so we can honestly check how well it
# generalizes to new data.

r2 = r2_score(y_test, y_pred)
# compares the model's predictions (y_pred) against the ACTUAL real values
# (y_test) and gives a single score from 0 to 1 (roughly): "what fraction of
# the variation in TotalAmount can this model explain."
mae = mean_absolute_error(y_test, y_pred)
# gives the average size of the model's mistakes, in the SAME units as
# TotalAmount (NPR) -- so "MAE = 562" literally means "on average, the
# model's guess is off by about NPR 562."

print(f"Q16a. Linear Regression Results:")
print(f"  R-squared: {r2:.4f}")
print(f"  MAE: NPR {mae:.2f}")
print("A high R-squared is expected here because TotalAmount is nearly a "
      "deterministic function of Quantity*UnitPrice — the model is mostly "
      "confirming that relationship, not discovering a subtle pattern.")

# Q16b: feature importance via coefficient magnitude (numeric features only,
# since one-hot encoded branch/category coefficients aren't directly comparable
# without standardization — reported qualitatively here).
num_feature_names = ["Quantity", "UnitPrice"]
# these stay as themselves after preprocessing (remember, remainder=
# "passthrough" left them untouched), so their names in the final feature
# list are unchanged.
coefs = model.named_steps["regressor"].coef_
# every trained LinearRegression model stores its learned coefficients (the
# "weight" it gave each input feature) in .coef_. named_steps["regressor"]
# reaches INTO the pipeline to grab the actual LinearRegression piece (as
# opposed to the "preprocess" piece) so we can access that.
cat_feature_names = list(
    model.named_steps["preprocess"].named_transformers_["cat"].get_feature_names_out(["Branch", "ProductCategory"])
)
# OneHotEncoder turns e.g. "Branch" into several new columns like
# "Branch_Kathmandu - Kupondole", "Branch_Pokhara - Lakeside", etc. This line
# asks the encoder to tell us exactly what it NAMED each of those new
# columns, so we can match them back up with their coefficients below.
all_names = cat_feature_names + num_feature_names
# combining both name lists into one list, in the SAME order the model
# actually used internally (one-hot columns first, then the untouched
# numeric ones) -- this order matters, it has to line up with "coefs" below.
coef_df = pd.DataFrame({"feature": all_names, "coefficient": coefs})
# build a proper table pairing each feature name with its learned
# coefficient, so it's readable instead of just a bare list of numbers.
coef_df["abs_coef"] = coef_df["coefficient"].abs()
# add a column with the ABSOLUTE value of each coefficient -- because a
# coefficient of -25 and +25 are both "large" in terms of influence, just in
# opposite directions; sorting by raw coefficient value would incorrectly
# treat -25 as "smaller" than +10.
print("\nQ16b. Top features by absolute coefficient size:")
print(coef_df.sort_values("abs_coef", ascending=False).head(10).to_string(index=False))
# sort by that absolute value, biggest first, keep the top 10, and
# .to_string(index=False) prints it as a clean table without pandas' default
# row-number column cluttering the output.
qty_coef = coef_df.loc[coef_df["feature"] == "Quantity", "coefficient"].iloc[0]
price_coef = coef_df.loc[coef_df["feature"] == "UnitPrice", "coefficient"].iloc[0]
# pull out just the Quantity and UnitPrice coefficients specifically, by
# name, so we can comment on them directly below. .loc[condition, column]
# filters rows matching that condition and grabs the specified column;
# .iloc[0] then grabs the single value out of the (one-row) result.
print(f"\nRaw coefficients aren't directly comparable across features on "
      f"different scales, so read them as local slopes, not importance ranks. "
      f"Quantity's coefficient (~{qty_coef:.0f}) approximates the average unit "
      f"price (~NPR {df['UnitPrice'].mean():.0f}) — makes sense since d(Total)/d(Qty) "
      f"= UnitPrice. UnitPrice's coefficient (~{price_coef:.2f}) approximates the "
      f"average basket quantity (~{df['Quantity'].mean():.1f}) for the same reason. "
      f"Branch and ProductCategory coefficients are much smaller, confirming they "
      f"add only marginal explanatory power once Quantity and UnitPrice are known — "
      f"as expected, since TotalAmount is built directly from those two.")
# this whole print is explaining WHY the numbers came out the way they did,
# not just reporting them: because TotalAmount = Quantity x UnitPrice, basic
# calculus says "if you increase Quantity by 1, TotalAmount increases by
# roughly whatever the UnitPrice was" -- and that's almost exactly what the
# model's Quantity coefficient turned out to be. Same logic in reverse for
# the UnitPrice coefficient. It's a nice sanity check that the model learned
# something real, not something random.

# =====================================================================
# STEP 17: BUSINESS INSIGHTS (printed summary — see write-up for full text)
# =====================================================================
print("\n" + "=" * 70)
print("STEP 17: KEY NUMBERS FOR THE INSIGHTS SECTION")
print("=" * 70)
print(f"Top branch by revenue: {branch_rev.idxmax()} (NPR {branch_rev.max():,.0f})")
# {:,.0f} formats a big number with comma separators (e.g. 5,988,127 instead
# of 5988127) and rounds off decimals -- purely for readability in a report.
print(f"Top city by revenue: {city_rev.idxmax()} (NPR {city_rev.max():,.0f})")
print(f"Top category by revenue: {cat_summary['Revenue'].idxmax()}")
print(f"Most common payment method: {df['PaymentMethod'].value_counts().idxmax()}")
print(f"Repeat customer rate: {repeat/(repeat+one_time)*100:.1f}%")
# repeat and one_time were calculated back in Step 13b -- this line reuses
# those same variables here to compute what PERCENTAGE of all customers are
# repeat shoppers, purely for a one-line summary stat.
print(f"Rows cleaned: {rows_before} -> {rows_after} "
      f"({rows_before - rows_after} duplicates removed)")
# reusing rows_before/rows_after from Step 6 -- pulling the cleaning result
# back up here so the "insights summary" section also documents the data
# quality work, not just the business numbers.

print("\n" + "=" * 70)
print("ALL DONE. Charts saved in ./outputs, cleaned CSV saved in ./outputs.")
print("=" * 70)