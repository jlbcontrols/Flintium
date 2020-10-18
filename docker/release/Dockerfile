FROM kcollins/ignition:8.0.12
USER root

# Gateway Backup
RUN curl -L -s "https://github.com/jlbcontrols/flintium/releases/download/v1.10.0-alpha0/backup.gwbk" -o /restore.gwbk

# Modules
RUN mkdir /modules && cd /modules && \
    curl -L -s "https://github.com/jlbreleases/pb-rel/releases/download/v1.10.2/pidbot-1.10.2-20200922.modl" -O && \
    curl -L -s "https://github.com/jlbcontrols/flintium-tag-config-tools/releases/download/v1.10.0-beta0/ftct-1.10.0-beta0-20201017.modl" -O

USER ${IGNITION_UID}
