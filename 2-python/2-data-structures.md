## The List

The "list" (often called an "array") is the simplest data type. It represents an **ordered collection** of other (usually similar) objects. Lists have length and contents. You can insert things into lists, as well as access things inside the list.

Lists are great when you have a handful of homogeneous or ordered items that you want to keep together, like names of band members:

```
['john', 'paul', 'george', 'ringo']
```

## The Dictionary

With lists, you access objects by their **location**. This is great when order matters, but there are lots of situations where order doesn't matter. In those situations, you usually want to access an objects by some sort of **key**.

Enter the "dictionary" (often called a "hash", for reasons that are very legitimate if not immediately apparent).

The dictionary has the property that every item is associated with a key. You use the key to set the value, you use the key to get the value. Dictionaries are great when you want to organize heterogenous data, like student records:

```
{
    'name': 'Isaac Harper'
    'uni': 'ish2321'
    'age': 27
}
```