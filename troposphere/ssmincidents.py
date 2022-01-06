# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 51.0.0


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer


class RegionConfiguration(AWSProperty):
    """
    `RegionConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-replicationset-regionconfiguration.html>`__
    """

    props: PropsDictType = {
        "SseKmsKeyId": (str, True),
    }


class ReplicationRegion(AWSProperty):
    """
    `ReplicationRegion <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-replicationset-replicationregion.html>`__
    """

    props: PropsDictType = {
        "RegionConfiguration": (RegionConfiguration, False),
        "RegionName": (str, False),
    }


class ReplicationSet(AWSObject):
    """
    `ReplicationSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html>`__
    """

    resource_type = "AWS::SSMIncidents::ReplicationSet"

    props: PropsDictType = {
        "DeletionProtected": (boolean, False),
        "Regions": ([ReplicationRegion], True),
    }


class SsmParameter(AWSProperty):
    """
    `SsmParameter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmparameter.html>`__
    """

    props: PropsDictType = {
        "Key": (str, True),
        "Values": ([str], True),
    }


class SsmAutomation(AWSProperty):
    """
    `SsmAutomation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmautomation.html>`__
    """

    props: PropsDictType = {
        "DocumentName": (str, True),
        "DocumentVersion": (str, False),
        "Parameters": ([SsmParameter], False),
        "RoleArn": (str, True),
        "TargetAccount": (str, False),
    }


class Action(AWSProperty):
    """
    `Action <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-action.html>`__
    """

    props: PropsDictType = {
        "SsmAutomation": (SsmAutomation, False),
    }


class ChatChannel(AWSProperty):
    """
    `ChatChannel <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-chatchannel.html>`__
    """

    props: PropsDictType = {
        "ChatbotSns": ([str], False),
    }


class NotificationTargetItem(AWSProperty):
    """
    `NotificationTargetItem <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-notificationtargetitem.html>`__
    """

    props: PropsDictType = {
        "SnsTopicArn": (str, False),
    }


class IncidentTemplate(AWSProperty):
    """
    `IncidentTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-incidenttemplate.html>`__
    """

    props: PropsDictType = {
        "DedupeString": (str, False),
        "Impact": (integer, True),
        "NotificationTargets": ([NotificationTargetItem], False),
        "Summary": (str, False),
        "Title": (str, True),
    }


class ResponsePlan(AWSObject):
    """
    `ResponsePlan <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html>`__
    """

    resource_type = "AWS::SSMIncidents::ResponsePlan"

    props: PropsDictType = {
        "Actions": ([Action], False),
        "ChatChannel": (ChatChannel, False),
        "DisplayName": (str, False),
        "Engagements": ([str], False),
        "IncidentTemplate": (IncidentTemplate, True),
        "Name": (str, True),
        "Tags": (Tags, False),
    }
