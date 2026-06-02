//Part 1: Basic MongoDB Queries
// 1. Display all customers
db.customers.find()

// 2. Display all restaurants
db.restaurants.find()

// 3. Display only customer name, city and membership
db.customers.find(
    {},
    {
        _id: 0,
        name: 1,
        city: 1,
        membership: 1
    }
)

// 4. Find all customers from Hyderabad
db.customers.find({
    city: "Hyderabad"
})

// 5. Find all Gold members
db.customers.find({
    membership: "Gold"
})

// 6. Find restaurants with rating greater than 4.5
db.restaurants.find({
    rating: { $gt: 4.5 }
})

// 7. Find orders with amount greater than ₹500
db.orders.find({
    order_amount: { $gt: 500 }
})

// 8. Find delivered orders
db.orders.find({
    order_status: "Delivered"
})

// 9. Find cancelled orders
db.orders.find({
    order_status: "Cancelled"
})

// 10. Find customers where phone is null
db.customers.find({
    phone: null
})

//Part 2: Operators

// 11. Find orders where amount is between ₹400 and ₹700
db.orders.find({
    order_amount: {
        $gte: 400,
        $lte: 700
    }
})

// 12. Find customers from Hyderabad, Delhi or Mumbai
db.customers.find({
    city: {
        $in: ["Hyderabad", "Delhi", "Mumbai"]
    }
})

// 13. Find restaurants whose cuisine is Indian or Fast Food
db.restaurants.find({
    cuisine: {
        $in: ["Indian", "Fast Food"]
    }
})

// 14. Find orders where payment status is not Success
db.orders.find({
    "payment.status": {
        $ne: "Success"
    }
})

// 15. Find orders where delivery time is null
db.orders.find({
    delivery_time_minutes: null
})

// 16. Find orders where rating is greater than or equal to 4
db.orders.find({
    order_rating: {
        $gte: 4
    }
})

// 17. Find restaurants not located in Bangalore or Chennai
db.restaurants.find({
    city: {
        $nin: ["Bangalore", "Chennai"]
    }
})

//Part 3: Array Queries

// 18. Find orders containing item Biryani
db.orders.find({
    "items.item_name": "Biryani"
})

// 19. Find orders containing item Pizza
db.orders.find({
    "items.item_name": "Pizza"
})

// 20. Find orders where any item quantity is greater than 1
db.orders.find({
    items: {
        $elemMatch: {
            quantity: { $gt: 1 }
        }
    }
})

// 21. Find orders where item price is greater than ₹300
db.orders.find({
    items: {
        $elemMatch: {
            price: { $gt: 300 }
        }
    }
})

// 22. Display only order ID and items
db.orders.find(
    {},
    {
        _id: 0,
        order_id: 1,
        items: 1
    }
)

//Part 4: Sorting and Limit

// 23. Sort restaurants by rating descending
db.restaurants.find().sort({
    rating: -1
})

// 24. Display top 3 highest rated restaurants
db.restaurants.find().sort({
    rating: -1
}).limit(3)

// 25. Sort orders by order amount descending
db.orders.find().sort({
    order_amount: -1
})

// 26. Display top 2 highest value orders
db.orders.find().sort({
    order_amount: -1
}).limit(2)

// 27. Sort delivery partners by rating descending
db.delivery_partners.find().sort({
    rating: -1
})

//Part 5: Update Operations

// 28. Update customer 1 membership to Platinum
db.customers.updateOne(
    { customer_id: 1 },
    { $set: { membership: "Platinum" } }
)

// 29. Update restaurant 104 rating to 4.1
db.restaurants.updateOne(
    { restaurant_id: 104 },
    { $set: { rating: 4.1 } }
)

// 30. Update order 1003 status to Delivered
db.orders.updateOne(
    { order_id: 1003 },
    { $set: { order_status: "Delivered" } }
)

// 31. Set delivery time of order 1003 to 45
db.orders.updateOne(
    { order_id: 1003 },
    { $set: { delivery_time_minutes: 45 } }
)

// 32. Add field active: true to all customers
db.customers.updateMany(
    {},
    { $set: { active: true } }
)

// 33. Remove field active from all customers
db.customers.updateMany(
    {},
    { $unset: { active: "" } }
)

// 34. Add a new item to order 1006
db.orders.updateOne(
    { order_id: 1006 },
    {
        $push: {
            items: {
                item_name: "Curd Rice",
                quantity: 1,
                price: 120
            }
        }
    }
)

//Part 6: Delete Operations

// 35. Delete cancelled orders
db.orders.deleteMany({
    order_status: "Cancelled"
})

// 36. Delete restaurants with rating less than 4.0
db.restaurants.deleteMany({
    rating: { $lt: 4.0 }
})

// Part 7: Count and Distinct

// 37. Count total customers
db.customers.countDocuments()

// 38. Count total orders
db.orders.countDocuments()

// 39. Count delivered orders
db.orders.countDocuments({
    order_status: "Delivered"
})

// 40. Count failed payments
db.orders.countDocuments({
    "payment.status": "Failed"
})

// 41. Display distinct customer cities
db.customers.distinct("city")

// 42. Display distinct restaurant cuisines
db.restaurants.distinct("cuisine")

// 43. Display distinct payment modes
db.orders.distinct("payment.mode")

// Part 8: Aggregation

// 44. Revenue by Payment Mode
db.orders.aggregate([
{
    $group: {
        _id: "$payment.mode",
        totalRevenue: { $sum: "$order_amount" }
    }
}
])

// 45. Revenue by Order Status
db.orders.aggregate([
{
    $group: {
        _id: "$order_status",
        totalRevenue: { $sum: "$order_amount" }
    }
}
])

// 46. Average Delivery Time
db.orders.aggregate([
{
    $match: {
        order_status: "Delivered"
    }
},
{
    $group: {
        _id: null,
        averageDeliveryTime: {
            $avg: "$delivery_time_minutes"
        }
    }
}
])

// 47. Orders by Customer
db.orders.aggregate([
{
    $group: {
        _id: "$customer_id",
        totalOrders: { $sum: 1 },
        totalAmount: { $sum: "$order_amount" }
    }
}
])

// 48. Orders by Restaurant
db.orders.aggregate([
{
    $group: {
        _id: "$restaurant_id",
        totalOrders: { $sum: 1 },
        totalRevenue: { $sum: "$order_amount" }
    }
}
])

// 49. Average Rating by Restaurant
db.orders.aggregate([
{
    $match: {
        order_rating: { $ne: null }
    }
},
{
    $group: {
        _id: "$restaurant_id",
        averageRating: { $avg: "$order_rating" }
    }
}
])

// 50. High Revenue Customers
db.orders.aggregate([
{
    $group: {
        _id: "$customer_id",
        totalSpending: { $sum: "$order_amount" }
    }
},
{
    $match: {
        totalSpending: { $gt: 700 }
    }
}
])

// Part 9: Lookup / Join Queries

// 51. Orders with Customer Details
db.orders.aggregate([
{
    $lookup: {
        from: "customers",
        localField: "customer_id",
        foreignField: "customer_id",
        as: "customer"
    }
},
{ $unwind: "$customer" },
{
    $project: {
        _id: 0,
        order_id: 1,
        customer_name: "$customer.name",
        city: "$customer.city",
        order_amount: 1,
        order_status: 1
    }
}
])

// 52. Orders with Restaurant Details
db.orders.aggregate([
{
    $lookup: {
        from: "restaurants",
        localField: "restaurant_id",
        foreignField: "restaurant_id",
        as: "restaurant"
    }
},
{ $unwind: "$restaurant" },
{
    $project: {
        _id: 0,
        order_id: 1,
        restaurant_name: "$restaurant.name",
        cuisine: "$restaurant.cuisine",
        order_amount: 1
    }
}
])

// 53. Orders with Delivery Partner Details
db.orders.aggregate([
{
    $lookup: {
        from: "delivery_partners",
        localField: "partner_id",
        foreignField: "partner_id",
        as: "partner"
    }
},
{ $unwind: "$partner" },
{
    $project: {
        _id: 0,
        order_id: 1,
        partner_name: "$partner.partner_name",
        delivery_time_minutes: 1,
        order_status: 1
    }
}
])

// 54. Full Order Report
db.orders.aggregate([
{
    $lookup: {
        from: "customers",
        localField: "customer_id",
        foreignField: "customer_id",
        as: "customer"
    }
},
{
    $lookup: {
        from: "restaurants",
        localField: "restaurant_id",
        foreignField: "restaurant_id",
        as: "restaurant"
    }
},
{
    $lookup: {
        from: "delivery_partners",
        localField: "partner_id",
        foreignField: "partner_id",
        as: "partner"
    }
},
{
    $unwind: "$customer"
},
{
    $unwind: "$restaurant"
},
{
    $unwind: {
        path: "$partner",
        preserveNullAndEmptyArrays: true
    }
},
{
    $project: {
        _id: 0,
        order_id: 1,
        customer_name: "$customer.name",
        restaurant_name: "$restaurant.name",
        cuisine: "$restaurant.cuisine",
        partner_name: "$partner.partner_name",
        order_amount: 1,
        payment_mode: "$payment.mode",
        payment_status: "$payment.status",
        order_status: 1,
        delivery_time_minutes: 1,
        order_rating: 1
    }
}
])

