// DATABASE
use EmployeeAttendanceDB

// COLLECTION
db.createCollection("staff_reviews")

// CREATE

// 1
db.staff_reviews.insertOne({
review_id: 1,
emp_id: 201,
emp_name: "Amit Verma",
department: "Engineering",
remarks: "Completed all assigned tasks on time",
score: 5,
review_date: new Date("2026-07-01")
})

// 2
db.staff_reviews.insertMany([
{
review_id: 2,
emp_id: 202,
emp_name: "Neha Gupta",
department: "Marketing",
remarks: "Very creative in campaigns",
score: 4
},
{
review_id: 3,
emp_id: 203,
emp_name: "Rohan Das",
department: "Operations",
remarks: "Maintains good attendance",
score: 5
}
])

// 3
db.staff_reviews.insertOne({
review_id: 4,
emp_id: 204,
emp_name: "Pooja Sharma",
metrics: {
projects_completed: 12,
attendance: 96
}
})

// 4
db.staff_reviews.insertOne({
review_id: 5,
emp_id: 205,
skills: ["leadership","communication","teamwork"]
})

// 5
let review = {
review_id: 6,
emp_id: 206,
emp_name: "Kishore",
score: 3
}
db.staff_reviews.insertOne(review)

// 6
db.staff_reviews.insertMany([
{
review_id: 7,
emp_id: 207,
emp_name: "Lavanya"
},
{
review_id: 8,
emp_id: 208,
emp_name: "Manoj"
}
])

// READ

// 1
db.staff_reviews.find()

// 2
db.staff_reviews.find(
{},
{
emp_name:1,
department:1,
score:1,
_id:0
}
)

// 3
db.staff_reviews.find({
score:{$gte:4}
})

// 4
db.staff_reviews.find().sort({
score:-1
})

// 5
db.staff_reviews.find().limit(3)

// 6
db.staff_reviews.aggregate([
{
$group:{
_id:"$department",
highestScore:{
$max:"$score"
}
}
}
])

// UPDATE

// 1
db.staff_reviews.updateOne(
{review_id:1},
{$set:{score:4}}
)

// 2
db.staff_reviews.updateMany(
{department:"Engineering"},
{$set:{department:"Tech"}}
)

// 3
db.staff_reviews.updateOne(
{review_id:2},
{$inc:{score:1}}
)

// 4
db.staff_reviews.updateMany(
{},
{$rename:{"remarks":"comments"}}
)

// 5
db.staff_reviews.updateOne(
{review_id:5},
{$push:{skills:"adaptability"}}
)

// 6
db.staff_reviews.updateOne(
{review_id:15},
{
$set:{
emp_name:"New Staff",
score:5
}
},
{
upsert:true
}
)

// DELETE

// 1
db.staff_reviews.deleteOne({
review_id:8
})

// 2
db.staff_reviews.deleteMany({
score:{$lt:3}
})

// 3
db.staff_reviews.deleteMany({
department:"Operations"
})

// 4
db.staff_reviews.deleteMany({
score:2
})

// 5
db.staff_reviews.deleteOne({
emp_id:206
})

// 6
db.staff_reviews.deleteMany({
emp_name:"New Staff"
})

// INDEXES

// 1
db.staff_reviews.createIndex({
emp_id:1
})

// 2
db.staff_reviews.createIndex({
department:1
})

// 3
db.staff_reviews.createIndex({
score:-1
})

// 4
db.staff_reviews.createIndex({
review_id:1
},{unique:true})

// 5
db.staff_reviews.createIndex({
comments:"text"
})

// 6
db.staff_reviews.getIndexes()
