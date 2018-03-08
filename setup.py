from setuptools import setup, find_packages


setup(
    name="btcpay",
    packages=find_packages(),
    version="1.0.3",
    description="Accept bitcoin with BTCPay",
    author="Joe Black",
    author_email="me@joeblack.nyc",
    url="https://github.com/joeblackwaslike/btcpay-python",
    download_url="https://github.com/joeblackwaslike/btcpay-python/tarball/v1.0.3",
    license='MIT',
    keywords=["bitcoin", "payments", "crypto"],
    install_requires=[
        "requests",
        "ecdsa"
    ],
    package_data={'': ['LICENSE']},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Office/Business :: Financial"
    ]
)
