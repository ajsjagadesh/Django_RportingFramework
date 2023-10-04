# FROM jfrog.fkinternal.com/fk-base-images/adoptopenjdk/jdk:8u322-debian11.3-slim-20220527

FROM jfrog.fkinternal.com/fk-base-images/debian:11.6-slim

ENV TZ="Asia/Kolkata"

RUN echo $TZ > /etc/timezone && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && dpkg-reconfigure --frontend noninteractive tzdata

# Create a new user and group with specific IDs
RUN groupadd -g 9876 fk-retail-platform
RUN useradd -g 9876 -u 4546 fk-vrp-001

# Installing Python and pip
RUN apt-get update
RUN apt-get install -y python3.9 && apt-get install -y python3-pip


# Set the working directory
WORKDIR /usr/src/fk-vrp-001

# Copy and install Python requirements
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

# Copy application files
COPY --chown=fk-vrp-001:fk-retail-platform . ./

# Make the entrypoint script executable
RUN chmod +x docker/entrypoint.sh

# Expose the port
EXPOSE 9090

# Set the entrypoint command
USER fk-vrp-001
ENTRYPOINT ["sh", "-c", "docker/entrypoint.sh"]