..
 This work is licensed under a Creative Commons Attribution 3.0 Unported
 License.
 http://creativecommons.org/licenses/by/3.0/legalcode

=============================
Role Assignment Notifications
=============================

`bp role-assignment-notifications
<https://blueprints.launchpad.net/keystone/+spec/role-assignment-notifications>`_

In the Juno release, expand on the notifications that are emitted from Keystone
by adding support for role assignments.

Problem Description
===================

Suppose a user maliciously decides to grant a role assignment to another user
he or she shouldn't have, or remove another user's role assignment. As of the
Icehouse release, it would only be possible to figure out the responsible
party by looking at Keystone logs. If Keystone were to emit notifications for
these types of events, auditing would become much easier.

Proposed Change
===============

1. Create a new decorator to emit CADF notifications for ``create_grant`` and
   ``delete_grant`` events.

2. Within the payload of the CADF notification should be the role id, the user
   id or group id (the actor), and the project id or domain id (the target).

Alternatives
------------

The admin may look at Keystone logs to find the responsible user; however, this
could be very hard to do, given the size of the log file.

Security Impact
---------------

None

Notifications Impact
--------------------

Create CADF notifications for ``create_grant`` and ``delete_grant`` at the
manager level of the assignment API.

Other End User Impact
---------------------

None

Performance Impact
------------------

None

Other Deployer Impact
---------------------

The audit events generated by the CADF notifications can now be audited.

Developer Impact
----------------

None

Implementation
==============

Assignee(s)
-----------

Primary assignee:

* stevemar (Steve Martinelli <stevemar@ca.ibm.com>)

Work Items
----------

* Expose ``create_grant`` to the manager level. Note that ``delete_grant`` is
  already exposed at the manager level.

* Create a new decorator specific to role assignments.

Dependencies
============

None

Documentation Impact
====================

Enhance the existing documentation to include the expected payload for a role
assignment event.

References
==========

* `Blueprint
  <https://blueprints.launchpad.net/keystone/+spec/role-assignment-notifications>`_

* `Notification Docs
  <docs.openstack.org/developer/keystone/event_notifications.html>`_
