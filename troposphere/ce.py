# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 51.0.0


from . import AWSObject, AWSProperty, PropsDictType
from .validators import double


class AnomalyMonitor(AWSObject):
    """
    `AnomalyMonitor <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html>`__
    """

    resource_type = "AWS::CE::AnomalyMonitor"

    props: PropsDictType = {
        "MonitorDimension": (str, False),
        "MonitorName": (str, True),
        "MonitorSpecification": (str, False),
        "MonitorType": (str, True),
    }


class Subscriber(AWSProperty):
    """
    `Subscriber <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalysubscription-subscriber.html>`__
    """

    props: PropsDictType = {
        "Address": (str, True),
        "Status": (str, False),
        "Type": (str, True),
    }


class AnomalySubscription(AWSObject):
    """
    `AnomalySubscription <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html>`__
    """

    resource_type = "AWS::CE::AnomalySubscription"

    props: PropsDictType = {
        "Frequency": (str, True),
        "MonitorArnList": ([str], True),
        "Subscribers": ([Subscriber], True),
        "SubscriptionName": (str, True),
        "Threshold": (double, True),
    }


class CostCategory(AWSObject):
    """
    `CostCategory <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html>`__
    """

    resource_type = "AWS::CE::CostCategory"

    props: PropsDictType = {
        "DefaultValue": (str, False),
        "Name": (str, True),
        "RuleVersion": (str, True),
        "Rules": (str, True),
        "SplitChargeRules": (str, False),
    }
