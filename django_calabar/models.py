from django.db import models


class TunnelConfig(models.Model):
    """
    A configuration object for a specific tunnel. This objects encapsulates the
    specific configuration file and options for its tunnel.
    """
    name = models.CharField(max_length=100, unique=True)
    """The Tunnel's name. Corresponds to its [tunnel:xxx] entry in the calabar configuration"""
    tunnel_type = models.CharField(max_length=30)
    """Type of network tunnel this instance represents. Validators are based on this"""
    cal_conf = models.TextField()
    """The text for this Tunnels entry in its calabar.conf"""
    tunnel_conf = models.TextField()
    """The contents of the configuration file for this specific tunnel type"""
    tunnel_conf_file = models.FileField('tunnel configuration file',
                                        upload_to=TunnelConfig.get_tunnel_conf_upload_dir,
                                        max_length=255,
                                        blank=True, null=True)
    """The tunnel configuration file for this specific tunnel"""

    def __unicode__(self):
        return u"Tunnel:<%s>" % self.name

    @staticmethod
    def get_tunnel_conf_upload_dir(instance, filename):
        """
        The upload path on which to store the :attr:`django_calabar.models.TunnelConfig.tunnel_conf_file`.

        Builds the location based on the CALABAR_UPLOAD_DIR setting.
        """
        path = os.path.join(
            settings.CALABAR_TUNNEL_CONF_UPLOAD_DIR,
            'tunnel_confs',
            "%s.conf" % instance.name,
        )
        return path


class CalabarConfig(models.Model):
    """
    A Calabar configuration object representing a set of tunnels and options.
    """
    name = models.CharField(max_length=100, unique=True)
    """This specific set of Tunnels' unique name"""
    global_conf = models.TextField()
    """The text for all non-tunnel configuration, like the ``[vpnc]`` section."""
    conf = models.TextField()
    """The entire contents of the configuration file from combining the global_conf
    and the configurations of each included tunnel"""
    conf_file = models.FileField('tunnel configuration file',
                                        upload_to=CalabarConfig.get_conf_upload_dir,
                                        max_length=255,
                                        blank=True, null=True)
    """The calabar configuration file."""
    tunnels = models.ManyToManyField(TunnelConfig)

    def __unicode__(self):
        return u"Calabar:<%s>" % self.name

    @staticmethod
    def get_conf_upload_dir(instance, filename):
        """
        The upload path on which to store the :attr:`django_calabar.models.TunnelConfig.tunnel_conf_file`.

        Builds the location based on the CALABAR_UPLOAD_DIR setting.
        """
        path = os.path.join(
            settings.CALABAR_TUNNEL_CONF_UPLOAD_DIR,
            "%s.conf" % instance.name,
        )
        return path
