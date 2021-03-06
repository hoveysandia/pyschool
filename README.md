![CI](https://github.com/hovey/pyschool/workflows/CI/badge.svg)

# pyschool
Examples of Best Practices and Pythonic Patterns

## Best Practices

## D.R.Y. it out

* `D.R.Y.` is don't repeat yourself.  
* `W.E.T.` is write everything twice.
* **Prefer dry code to wet code.**

Dry code appears in the code base one and *only* one time.  Code that appears more than once it is not dry, it is wet.  

When code is repeated `[2, 3, ...n]` times, it creates two code liabilities:

1. **Maintainence** - a change to dry code requires only one update; the change is isolated to one location in the code base.  A change to wet code requires that all instances of the code snippet be updated, a tedious and potentially time consuming task when the repeated code is pervasive throughout the code base.  A project-wide search and replace may help find all instances, but requires additional maintainence effort.  
2. **Bugs** -  moreover, wet code can be highly error prone.  A lurking instance of wet code that was not discovered when a maintainence update ocurred exposes the developer to risk code bugs stemming from unanticipated behavior.

## Convention > Configuration

Code should just run the first time, without clients needing to spend excessive amount of time configuring prior to the run.  Services should use default values.  Allow clients to modify the default values through the service's API.

## Kill all non-C.R.U.D. verbs in APIs

`Get` and `Set` are dead weight verbs that can be inferred from whether a value is being returned (a getter) or passed (a setter).  When `get` and `set` are eliminated from the API, client code gets more compact, more noun-driven, more attribute-rich, and less procedural.  

Consider
```python
  set_color(self, value):  # bloated
    self._color = value
```
versus
```python
  color(self, value):  # not bloated
    self._color = value
 ```

Verbs, in general, can harbor lots of dead weight and bloat.  Instead of `set` other verbs that could be used with `color` are `calculate` (e.g., RBG or alpha channels) or `update` or `render` or `draw` or `paint` or `apply`... and really these verbs are hallmarks of implementation, not interface; they start to expose the service's internals for returning a color to the client.  And, they are unnecessary noise for the client, who either just wants to get or set the color, and not worry about how the same is implemented. 

Thus, verbs, *in the service API*, invite the slippery slope of coupling client to a service's implementation, which is bad.  Prefer to couple the client to the service's interface.  That way, should the implementation change, it does not propagate changes to the client, forcing them to update how they use the service.

### C.R.U.D.

From the database standard, there are four main verbs that span all tranactions: 

* **CREATE** - aka calculate, compute, evaluate, generate, make, new
* **READ** *this is **get***, copy, fetch, serialize (with read)
* **UPDATE** *this is **set***, serialize (with write), write
* **DELETE** typically not used except for memory management, or dropping a record from a database

## Code Smell

Consider the string of `if` checking:
```python
  if barks:
    # do something with Dog objects
  
  if meows:
    # do something with Cat objects
    
  if tweets:
    # do something with Bird objects
```

This is an example of `code smell`, which means the code has sufficent *function* but has weak *form*.  In this example, the client is forever checking the myriad of different `Animal` descendants.  As the number of `Animals` increases, clients must modify their code everyhere they used this smelly pattern.  

## Client-Service Decoupling

Services should expose client functionality through a service API.  The API will be better when it [avoids verbs](README.md#kill-all-non-crud-verbs-in-apis).  Services should not expose implementation.  

Clients should code to a service's interface, not implementation.  This allows the client to be only loosely coupled to the service, which is good.  Tight coupling is bad.  Loose coupling allows the client and the service to change over time independent from one another.  A change to the service that also requires a change to any and all clients who have used the service in the past is an example of [code smell](README.md#code-smell).



## Pythonic Patterns

### Attributes

* See the [`get_set` example](get_set/README.md), which goes through a short code example, with evolution from bad, to better, to best implementations.  

### Client-Service

* To come.

### Decorators

* An [example](logging_decorator.py) of a logging decorator pattern, which can help D.R.Y. out code (based on [this example](http://book.pythontips.com/en/latest/decorators.html#logging)).
* An [example](decorators.py), using factorial, `tic-toc` timing convention, and [memoization](https://en.wikipedia.org/wiki/Memoization).
* See also [Real Python](https://realpython.com/primer-on-python-decorators/), [Wiki Python](https://wiki.python.org/moin/PythonDecorators), [Yasoob Khalid](http://book.pythontips.com/en/latest/decorators.html)

### Docstrings

* See [Google docstring format](http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)

### Error Checking (ask for forgiveness, not permission)

* See [examples](error_check.md).

### [Factory](factory.md)


### Import

* When [importing modules](importable/importable.md) from non-local directories.  Used often in client-service patterns.

### Inheritance

* A compact [example](inheritance_farm/readme.txt), showing a verb astraction (e.g., `speak`) and inheritance of behavior, with a simple client-service architecture.
* [shapes](super/shapes.py)

### Iteration

* See [`for_loop_vs_iterator.py`](for_loop_v_iterator.py) for an example.

### Model, View, Controller (MVC)

* [shapes_mvc](super/shapes_mvc.py)

### Unit Test

* An [example](test_unittest.py), using the [unittest.mock](https://docs.python.org/3/library/unittest.mock.html#) library for testing in Python.
* [Real Python](https://realpython.com/python-mock-library/) article.  

## Examples

### Computation

* [Ordinary least squares](least_squares/ols.py)
* Several examples in the `monkey_see` folder  

### Matplotlib

* [Anatomy of a figure](anatomy_of_figure/anatomy_of_figure.py), a reproduction of a well-known exposition of features available in Matplotlib.
* [Element scale versus density](element_scale_v_density/element_scale_v_density.py), an example of a log-scale plot.
* [Growth Charts](growth_charts/README.md), attributes of error checking, kwarg forwarding, fill between, and color transparency.
* [Introductory tutorials](introductory_tutorials.py)
* [Quartiles](quartiles/pfield.py)

### Production

Once the code base has sufficient development, and it is ready for production, use the following steps:

* TLC - timing, leaks, [coverage](https://github.com/marketplace/actions/coveralls-github-action)
* Test
  * Unit Test
  * Integration Test
* [Packaging](https://packaging.python.org/tutorials/packaging-projects/) (Build, Installer), and packaging [guide](https://packaging.python.org/guides/distributing-packages-using-setuptools/)
* [Distribution](https://pypi.org/) with PyPI
* Client Use
  * Client [Installation](https://packaging.python.org/tutorials/installing-packages/)
  * Client Bug Reports (https://github.com/hovey/pyschool/issues)

## References

* [Effective-Python](https://hacktec.gitbooks.io/effective-python/content/en/Chapter1/Chapter1.html)
* [GitHub build badge](https://help.github.com/en/actions/configuring-and-managing-workflows/configuring-a-workflow#adding-a-workflow-status-badge-to-your-repository)

