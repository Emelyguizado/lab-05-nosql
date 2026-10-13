// Step 2: 
// use bookstore 
db = db.getSiblingDB("bookstore")

// Step 3: load authors.json
db.authors.drop()
doc = JSON.parse(fs.readFileSync("authors.json", "utf8"))
db.authors.insertMany(doc)

// Step 4: load books.json
db.books.drop()
doc = JSON.parse(fs.readFileSync("books.json", "utf8"))
db.books.insertMany(doc)

// Step 5: list authors and books
db.authors.find()
db.books.find()

// Step 6: insert two new books
db.books.insertOne({title: "Don Quixote", published_year: 1605, author_ids: ['author_004'] })
db.books.insertOne({title: "Emma", published_year: 1815, author_ids: ['author_001'] })

// Step 7: add missing authors
db.authors.insertOne({_id:'author_004', name: 'Miguel de Cervantes', nationality:'Spanish',bio: { short: "Spanish novelist, poet, and playwright.", long: "Miguel de Cervantes was a Spanish writer best known for Don Quixote, widely considered one of the first modern novels and one of the greatest works of Western literature." }})

// Step 8: filter books by a list of authors
db.books.find({ author_ids: { $in: ["author_001", "author_004"] } })

