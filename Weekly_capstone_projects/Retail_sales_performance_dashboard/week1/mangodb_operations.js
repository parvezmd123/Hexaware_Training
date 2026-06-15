// DATABASE
use RetailSalesDB

// Create Collection & Insert Data
db.campaign_feedback.insertMany([
{
    campaign_id: 1,
    product_id: 101,
    product_name: "Laptop",
    region: "South",
    customer_name: "Rahul",
    rating: 5,
    feedback: "Excellent discount campaign",
    campaign_date: new Date("2026-06-01")
},
{
    campaign_id: 2,
    product_id: 102,
    product_name: "Mobile",
    region: "South",
    customer_name: "Priya",
    rating: 4,
    feedback: "Good cashback offer",
    campaign_date: new Date("2026-06-02")
},
{
    campaign_id: 3,
    product_id: 103,
    product_name: "Headphones",
    region: "West",
    customer_name: "Kiran",
    rating: 3,
    feedback: "Average promotion",
    campaign_date: new Date("2026-06-03")
}
]);

// ----------------------
// CREATE OPERATIONS
// ----------------------

// 1
db.campaign_feedback.insertOne({
    campaign_id: 4,
    product_id: 101,
    product_name: "Laptop",
    region: "North",
    customer_name: "Anjali",
    rating: 5,
    feedback: "Loved the offer"
});

// 2
db.campaign_feedback.insertOne({
    campaign_id: 5,
    product_id: 102,
    product_name: "Mobile",
    region: "West",
    customer_name: "Vijay",
    rating: 4,
    feedback: "Worth buying"
});

// 3
db.campaign_feedback.insertMany([
{
    campaign_id: 6,
    product_id: 103,
    product_name: "Headphones",
    region: "South",
    customer_name: "Meena",
    rating: 5,
    feedback: "Very useful"
},
{
    campaign_id: 7,
    product_id: 101,
    product_name: "Laptop",
    region: "East",
    customer_name: "Arun",
    rating: 4,
    feedback: "Satisfied"
}
]);

// ----------------------
// READ OPERATIONS
// ----------------------

// 1
db.campaign_feedback.find();

// 2
db.campaign_feedback.find({ product_name: "Laptop" });

// 3
db.campaign_feedback.find({ region: "South" });

// 4
db.campaign_feedback.find({ rating: { $gte: 4 } });

// 5
db.campaign_feedback.find(
    {},
    {
        customer_name: 1,
        product_name: 1,
        rating: 1,
        _id: 0
    }
);

// 6
db.campaign_feedback.find().sort({ rating: -1 });

// ----------------------
// UPDATE OPERATIONS
// ----------------------

// 1
db.campaign_feedback.updateOne(
    { campaign_id: 4 },
    { $set: { rating: 4 } }
);

// 2
db.campaign_feedback.updateOne(
    { campaign_id: 5 },
    { $set: { region: "South" } }
);

// 3
db.campaign_feedback.updateMany(
    { product_name: "Laptop" },
    { $set: { feedback: "Updated Laptop Campaign" } }
);

// 4
db.campaign_feedback.updateOne(
    { customer_name: "Meena" },
    { $set: { rating: 5 } }
);

// 5
db.campaign_feedback.updateMany(
    { rating: 3 },
    { $set: { rating: 4 } }
);

// 6
db.campaign_feedback.updateOne(
    { campaign_id: 7 },
    { $set: { customer_name: "Arunkumar" } }
);

// ----------------------
// DELETE OPERATIONS
// ----------------------

// 1
db.campaign_feedback.deleteOne({
    campaign_id: 7
});

// 2
db.campaign_feedback.deleteOne({
    customer_name: "Vijay"
});

// 3
db.campaign_feedback.deleteMany({
    rating: { $lt: 4 }
});

// 4
db.campaign_feedback.deleteMany({
    region: "East"
});

// 5
db.campaign_feedback.deleteOne({
    campaign_id: 6
});

// 6
db.campaign_feedback.deleteMany({
    product_name: "Headphones"
});

// ----------------------
// AGGREGATION QUERIES
// ----------------------

// 1 Total feedback count by product
db.campaign_feedback.aggregate([
{
    $group: {
        _id: "$product_name",
        total_feedback: { $sum: 1 }
    }
}
]);

// 2 Average rating by product
db.campaign_feedback.aggregate([
{
    $group: {
        _id: "$product_name",
        average_rating: { $avg: "$rating" }
    }
}
]);

// 3 Feedback count by region
db.campaign_feedback.aggregate([
{
    $group: {
        _id: "$region",
        total_feedback: { $sum: 1 }
    }
}
]);

// 4 Highest rated products
db.campaign_feedback.aggregate([
{
    $group: {
        _id: "$product_name",
        avg_rating: { $avg: "$rating" }
    }
},
{
    $sort: {
        avg_rating: -1
    }
}
]);

// 5 Count feedback with rating >= 4
db.campaign_feedback.countDocuments({
    rating: { $gte: 4 }
});

// 6 Distinct regions
db.campaign_feedback.distinct("region");

// ----------------------
// INDEXES
// ----------------------

// 1
db.campaign_feedback.createIndex({
    product_name: 1
});

// 2
db.campaign_feedback.createIndex({
    region: 1
});

// 3
db.campaign_feedback.createIndex({
    customer_name: 1
});

// 4
db.campaign_feedback.createIndex({
    rating: -1
});

// 5
db.campaign_feedback.createIndex({
    campaign_date: 1
});

// 6
db.campaign_feedback.createIndex({
    product_name: 1,
    region: 1
});

// Verify Indexes
db.campaign_feedback.getIndexes();
