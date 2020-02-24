import pymongo
import bottle
import sys

#Specify the Connection Parameters to Localhost

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.test          # attach to db
collec_albums = db.albums     # specify the colllection
collec_images = db.images
collec_imglist = db.imglist

#Print the initial collection counts
print "Album Count: ",collec_albums.count()
print "Images Count: ",collec_images.count()

#Print the Image Count Prior to the Delete
Img_CkCur = db.images.aggregate([{"$project":{"tags":1,"_id":0}},{"$unwind":"$tags"},
                         {"$match":{"tags":"kittens"}},{"$group":{"_id":"$tags","count":{"$sum":1}}}])

for idoc in Img_CkCur['result']:
    print 'Total Images(Kitten) Records',idoc['count']

for doc in Img_base['result']:
    myCursor = collec_albums.find({"images":{"$eq" :doc['_id']}}).count()
    if myCursor != 0:
        continue
    else:
        print 'Removing',doc['_id']
        collec_images.remove({"_id":{"$eq" :doc['_id']}})

#Print the Image Count Post Delete

Img_CkCurF = db.images.aggregate([{"$project":{"tags":1,"_id":0}},{"$unwind":"$tags"},
                         {"$match":{"tags":"kittens"}},{"$group":{"_id":"$tags","count":{"$sum":1}}}])
#For Loop
for idoc in Img_CkCurF['result']:
    print 'Total Images(Kitten) Records(Post Removal)',idoc['count']





