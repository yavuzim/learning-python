import pandas as pd

df = pd.read_csv("youtube-ing.csv")

print(df)
print(df.columns)

# 1- İlk 10 kaydı getiriniz.
sonuc = df.head(10)
# 2- İkinci 5 kaydı getiriniz.
sonuc = df[5:].head(5)

# 3- Dataset' de bulunan kolon isimleri ve sayısını bulunuz.
sonuc = df.columns
sonuc = len(df.columns)

# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz.
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)
df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"],axis=1,inplace=True)

# 5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz.
sonuc = df[["likes","dislikes"]].mean()
sonuc = df["likes"].mean()
sonuc = df["dislikes"].mean()

# 6- ilk 50 videonun like ve dislike kolonlarını getiriniz.
sonuc = df.loc[:49,["likes","dislikes"]]
sonuc = df[["likes","dislikes"]].head(50)

# 7- En çok görüntülenen video hangisidir ?
sonuc = df[(df["views"]==df["views"].max())][["title","views"]]

# 8- En düşük görüntülenen video hangisidir?
sonuc = df[(df["views"]==df["views"].min())][["title","views"]]
sonuc = df[(df["views"]==df["views"].min())]["title"].iloc[0] # sttr olarak verir.

# 9- En fazla görüntülenen ilk 10 video hangisidir ?
sonuc = df.sort_values("views",ascending=False)[["title","views"]].head(10)

# 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.
sonuc = df.groupby("category_id").mean().sort_values("likes")["likes"]

# 11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.
sonuc = df.groupby("category_id").sum().sort_values("comment_count",ascending=False)["comment_count"]

# 12- Her kategoride kaç video vardır ?
sonuc = df["category_id"].value_counts()

# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.
df["sonuc"] = df["title"].str.len()
df["sonuc"] = df["title"].apply(len)
sonuc = df["sonuc"] 

# 14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.
df["tagkolon"] = df["tags"].apply(lambda x: len(x.split("|")))
sonuc = df["tagkolon"]

# 15- En popüler videoları listeleyiniz.(like/dislike oranına göre)
def oran(veri):
    likesListe = list(veri["likes"])
    dislikeListe = list(veri["dislikes"])    
    liste = list(zip(likesListe,dislikeListe)) # (1020,230), (201,233)
    oranListesi = []
    for like,dislike in liste:
        if (like+dislike) == 0:
            oranListesi.append(0)
        else: 
            oranListesi.append(like/(like+dislike))
    return oranListesi    

df["begeni_orani"] = oran(df)
sonuc = df.sort_values("begeni_orani",ascending=False)[["title","likes","dislikes","begeni_orani"]]