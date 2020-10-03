from setuptools import setup, find_packages


setup(
    name="btcpay-python",
    packages=find_packages(),
    version="1.3.0",
    description="Accept bitcoin with BTCPay",
    url="https://github.com/btcpayserver/btcpay-python",
    download_url="https://github.com/btcpayserver/btcpay-python/archive/v1.3.0.tar.gz",
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
