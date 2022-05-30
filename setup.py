from setuptools import setup, find_packages


install_requires = ["requests~=2.25.1", "spacy~=2.2.4"]

setup(
    name="Mbaza",
    version="1.0",
    description="Mbaza AI Chatbot",
    author="Digital Umuganda",
    author_email="",
    maintainer="Charles Yusuf",
    maintainer_email="charles@digitalumuganda.com",
    url="ssh://git@git.risa.gov.rw:2222/risa/risa-gcino-projects/risa-innovation-division-projects/mbaza-chatbot/mbaza-chatbot-rasa-implementation/mbaza-chatbot-rasa-language-model-english.git",  # to be updated when in open source
    packages=find_packages("mbaza-chatbot-rasa-language-model-english"),
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Developers",
        # supported python versions
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=install_requires,
)
