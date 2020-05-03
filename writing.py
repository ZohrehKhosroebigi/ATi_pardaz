# Python3 implementation of the approach  
"""
# Function to return the
# intersection set of s1 and s2
def intersection(s1, s2):
    # Find the intersection of the two sets
    intersect = s1 & s2;

    return intersect;


# Function to return the Jaccard index of two sets
def jaccard_index(s1, s2):
    # Sizes of both the sets
    size_s1 = len(s1);
    size_s2 = len(s2);

    # Get the intersection set
    intersect = intersection(s1, s2);

    # Size of the intersection set
    size_in = len(intersect);

    # Calculate the Jaccard index
    # using the formula
    jaccard_in = size_in / (size_s1 + size_s2 - size_in);

    # Return the Jaccard index
    return jaccard_in;


# Function to return the Jaccard distance
def jaccard_distance(jaccardIndex):
    # Calculate the Jaccard distance
    # using the formula
    jaccard_dist = 1 - jaccardIndex;

    # Return the Jaccard distance
    return jaccard_dist;


# Driver code
if __name__ == "__main__":
    # Elements of the 1st set
    str1='«برداشت کارشناسی»، «جو روانی» و «بازارهای رقیب» قابل محاسبه و تحٶلیل است که'
    words=str1.split()
    s1 = set();
    for word in words:
        s1.add(word);

    # Elements of the 2nd set
    s2 = set();
    str2 = '«برداشت کارشناسی»، «جو روانی» و «سلام عزیزم» قابل محاسبه و تحٶلیل نیست که'
    words = str2.split()
    for word in words:
        s2.add(word);

    jaccardIndex = jaccard_index(s1, s2);

    # Print the Jaccard index and Jaccard distance
    print("Jaccard index = ", jaccardIndex);
    print("Jaccard distance = ", jaccard_distance(jaccardIndex));

    # This code is contributed by AnkitRai01
"""
str1='«برداشت کارشناسی»، «جو روانی» و «بازارهای رقیب» قابل محاسبه و تحٶلیل است که'
str2 = '«برداشت کارشناسی»، «جو روانی» و «سلام عزیزم» قابل محاسبه و تحٶلیل نیست که'
"""a = set(str1.split())
b = set(str2.split())
c = a.intersection(b)
jacard_index=float((len(c)) / (len(a) + len(b) - len(c)))
jacard_ditanc=1-jacard_index
print( jacard_index)
print( jacard_ditanc)"""

query=str1.split()
document=str2.split()
intersection = set(query).intersection(set(document))
union = set(query).union(set(document))
print(len(intersection)/len(union))