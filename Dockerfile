FROM python:3.6
MAINTAINER flip387@gmail.com

# Install deps
RUN apt-get update && apt-get install -y \
  python-dev \
  python-pip

# Add project source to docker container
ADD . /root/
WORKDIR /root/

# Install project reqs
RUN pip install -r requirements.txt

# Install project
RUN python setup.py develop

# Run project
ENTRYPOINT ["circle_test"]
CMD []
