#############################################
# Select the OS
FROM python:3.8

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libopenslide0 \
        libtk8.6 \
        procps \
        zip \
    && rm -rf /var/lib/apt/lists/*

#############################################
# Setup default flywheel/v0 directory
ENV FLYWHEEL=/flywheel/v0
RUN mkdir -p ${FLYWHEEL}

COPY HistoQC $FLYWHEEL/
COPY *.txt $FLYWHEEL/
COPY *.py $FLYWHEEL/
COPY *.sh $FLYWHEEL/
COPY *.json $FLYWHEEL/

WORKDIR ${FLYWHEEL}

#############################################
# install HistoQC required dependencies
RUN pip install -r requirements.txt

# Install Flywheel main deps
RUN pip install flywheel-gear-toolkit
RUN pip install flywheel-sdk
RUN pip install fw-core-client

#############################################
# Configure entrypoint
RUN chmod a+x /flywheel/v0/run
ENTRYPOINT ["./flywheel/v0/run"]
