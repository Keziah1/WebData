from rdflib import Graph, URIRef, Namespace, RDF

path = "ProjectWeb2.rdf"
g = Graph()
g.parse(path, format="xml")

ns = Namespace("http://schema.org/#")

# Question 1
for client in g.subjects(predicate=RDF.type, object=ns.Restaurant):
    print(client)

#Question 2
query = """
PREFIX fd: <http://schema.org/#>
SELECT ?Restaurant
WHERE {
  {
    ?Restaurant rdf:type fd:FastFoodRestaurant .
  }
  UNION
  {
    ?Restaurant rdf:type fd:HealthyRestaurant .
  }
  UNION
  {
    ?Restaurant rdf:type fd:ItalianRestaurant .
  }
}
"""

results = g.query(query)

for row in results:
    print(row['Restaurant'])


# #Question 3
# for restaurant in g.subjects(predicate=URIRef(ns.serves), object=URIRef(ns.ItalianFood)):
#     print(restaurant)

