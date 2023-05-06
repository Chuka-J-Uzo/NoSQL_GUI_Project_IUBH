( { quantity: { $lt: 50 } } ) 


### Delete a collection
        db.Data_collection.deleteMany({})
	
### Merge two fields
        db.Data_collection.updateMany({}, { $set: { merged_field: { $concat: ["$price", " ", "$quantity"] } } }, { multi: true })
### Rename a fields       
        db.Data_collection.updateOne({item: "Item 1"}, {$rename: {"category": "Category 1"}})
### Remove a field       
        db.Data_collection.updateOne({item: "Item 1"}, {$unset: {size: ""}})
### Add a field        
        db.Data_collection.updateOne({item: "Item 1"}, {$set: {"Size": "Medium"}})
        
### Do a conditional update for several fields
	db.Data_collection.updateMany(
  { category: "Category 1" },
  {
    $set: {
      price: { $multiply: ["$price", 1.1] },
      quantity: { $subtract: ["$quantity", 10] },
      brand: "New Brand"
    }
  }
)

       
### Add a field to a particular position
	       db.Data_collection.aggregate([
	  {
	    $match: { item: "Item 1" }
	  },
	  {
	    $addFields: {
	      Size: "Medium"
	    }
	  },
	  {
	    $project: {
	      _id: 0,
	      item: 1,
	      price: 1,
	      quantity: 1,
	      category: 1,
	      brand: 1,
	      color: 1,
	      Size: 1,
	      material: 1
	      
	    }
	  }
	])



### Check to see if the merge works
 	db.Data_collection.find().pretty()

