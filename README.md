# YAP Python Library
The YAP Python library provides convenient access to the YAP API from applications written in the Python language.

## Requirements
-   Python 2.7+ or Python 3.6+

## Installing

It's an official version for Python

```
pip install --upgrade yap-sdk
```

Enjoy 🎉

## Usage

The library needs to be configured with your account's secret key which is
available in your [YAP Dashboard][api-keys]:

```python
from yapsdk import Yap

service = Yap(api_key='...')

# detect faces on document
response = service.detect_faces(content='/9j/4AAQSkZJRgABAQEASABIA....')

# print that response
print(response.faces)
```

## Example
List of examples for quickly start on your project.

| Features                  | File                                                                                                      |
|---------------------------|-----------------------------------------------------------------------------------------------------------|
| Extract text              | [text.py](https://github.com/youngapp/yap-python/blob/develop/examples/text.py)                           |
| Extract lines             | [line.py](https://github.com/youngapp/yap-python/blob/develop/examples/line.py)                           |
| Extract table             | [table.py](https://github.com/youngapp/yap-python/blob/develop/examples/table.py)                         |
| Get entities              | [entities.py](https://github.com/youngapp/yap-python/blob/develop/examples/entities.py)                   |
| Get dominant language     | [dominant_language.py](https://github.com/youngapp/yap-python/blob/develop/examples/dominant_language.py) |
| Detect faces              | [detect_faces.py](https://github.com/youngapp/yap-python/blob/develop/examples/detect_faces.py)           |
| Compare faces             | [compare_faces.py](https://github.com/youngapp/yap-python/blob/develop/examples/compare_faces.py)         |

## Opening issues

If you encounter a bug with YAP, we would appreciate if you inform us about it.
Before opening a new issue, please go through [existing issues](https://github.com/youngapp/yap-python/issues)
to find the solution right away if your problem was solved before.

Attach the following details if appropriate:

-   SDK
-   Python version
-   Environment and OS
-   Stack trace

The GitHub issues are intended for bug reports and feature requests.
For quick help and questions on using the Yap SDK for Python, please use the resources listed within [Getting Help](https://github.com/youngapp/yap-python#getting-help) section. The time of our support experts is rushingly flying but even so, they would like to help you in time, and therefore, will appreciate your help in applying for support reasonably by providing full details and excluding duplicated issues.

## Contribute

Yap is the open source and we love contributions! If you have an idea for a great improvement or spy an issue you’re keen to fix, follow our [Contributing Guide](https://github.com/youngapp/yap-python/blob/master/CONTRIBUTING.md).

No contribution is too small – we encourage you to provide feedback and [report issues](https://github.com/youngapp/yap-python/issues).

## Community support 🌍

For general help using Yap, please refer to [the official Yap documentation](https://developer.youngapp.co/). For additional help, you can use one of these channels to ask a question:

-   [StackOverflow](http://stackoverflow.com/questions/tagged/yap-python)
-   [GitHub](https://github.com/youngapp/yap-python) (Bug reports, feature requests, contributions)
-   [Twitter](https://twitter.com/youngapp_pf) (Get the news fast)
-   [YouTube Channel](https://www.youtube.com/channel/UCPY1PeAXPQIgo29e4Z9u5cA) (Learn from Video Tutorials)

## License

This SDK is distributed under Commerciale License.

