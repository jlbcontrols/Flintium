FROM kcollins/ignition:8.0.12
USER root

# Modules
RUN mkdir /modules && cd /modules && \
    curl -L -s "https://github.com/jlbreleases/pb-rel/releases/download/v1.10.2/pidbot-1.10.2-20200922.modl" -O && \
    curl -L -s "https://github.com/jlbcontrols/flintium-tag-config-tools/releases/download/v1.10.0-beta0/ftct-1.10.0-beta0-20201017.modl" -O

# Create projects folder
RUN mkdir /var/lib/ignition/data/projects

# Match typical linux user/group so host and container users have bind mount permission. (TODO: Make this a build arg instead)
ENV IGNITION_UID=1000
ENV IGNITION_GID=1000

# Modify user/group from base image, and update file ownership.
RUN usermod -u ${IGNITION_UID} ignition && groupmod -g ${IGNITION_GID} ignition
RUN chown -R ${IGNITION_UID}:${IGNITION_GID} ${IGNITION_INSTALL_LOCATION} ${IGNITION_INSTALL_USERHOME} /var/lib/ignition /var/log/ignition

USER ${IGNITION_UID}


