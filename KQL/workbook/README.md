# Example
```
{
  "version": "Notebook/1.0",
  "items": [
    {
      "type": 12,
      "content": {
        "version": "NotebookGroup/1.0",
        "groupType": "editable",
        "items": [
          {
            "type": 1,
            "content": {
              "json": "![Image Title](weblink to Image)\r\n\r\n# Company Name\r\n## <subtitle> ie. Monthly Managed Security Services Review"
            },
            "name": "text - 0"
          },
          {
            "type": 12,
            "content": {
              "version": "NotebookGroup/1.0",
              "groupType": "editable",
              "items": [
                {
                  "type": 1,
                  "content": {
                    "json": "Created on: "
                  },
                  "customWidth": "15",
                  "name": "text - 3"
                },
                {
                  "type": 3,
                  "content": {
                    "version": "KqlItem/1.0",
                    "query": "Heartbeat\r\n| where TimeGenerated <= ago(3h)\r\n| project format_datetime(TimeGenerated, 'MM-dd-yyyy')\r\n| top 1 by TimeGenerated",
                    "size": 3,
                    "timeContext": {
                      "durationMs": 2592000000
                    },
                    "queryType": 0,
                    "resourceType": "microsoft.operationalinsights/workspaces",
                    "visualization": "card"
                  },
                  "customWidth": "85",
                  "name": "query - 4"
                },
                {
                  "type": 1,
                  "content": {
                    "json": "For the time period of: "
                  },
                  "customWidth": "25",
                  "name": "text - 2"
                },
                {
                  "type": 3,
                  "content": {
                    "version": "KqlItem/1.0",
                    "query": "// 1 month period not including this month\r\nlet StartofMonth = startofmonth(datetime(now), -1);\r\nlet EndofMonth = endofmonth(datetime(now), -1);\r\nHeartbeat\r\n| where TimeGenerated <= ago(3h)\r\n| project ['Start Date'] = format_datetime(StartofMonth, 'MM-dd-yyyy')\r\n| top 1 by EndofMonth",
                    "size": 3,
                    "timeContext": {
                      "durationMs": 2592000000
                    },
                    "queryType": 0,
                    "resourceType": "microsoft.operationalinsights/workspaces",
                    "visualization": "card"
                  },
                  "customWidth": "20",
                  "name": "query - 3"
                },
                {
                  "type": 1,
                  "content": {
                    "json": "to"
                  },
                  "customWidth": "2",
                  "name": "text - 5"
                },
                {
                  "type": 3,
                  "content": {
                    "version": "KqlItem/1.0",
                    "query": "// 1 month period not including this month\r\nlet StartofMonth = startofmonth(datetime(now), -1);\r\nlet EndofMonth = endofmonth(datetime(now), -1);\r\nHeartbeat\r\n| where TimeGenerated <= ago(3h)\r\n| project ['End Date'] = format_datetime(EndofMonth, 'MM-dd-yyyy')\r\n| top 1 by EndofMonth",
                    "size": 3,
                    "timeContext": {
                      "durationMs": 2592000000
                    },
                    "queryType": 0,
                    "resourceType": "microsoft.operationalinsights/workspaces",
                    "visualization": "card"
                  },
                  "customWidth": "20",
                  "name": "query - 5"
                }
              ]
            },
            "name": "group - 3"
          },
          {
            "type": 1,
            "content": {
              "json": "## Company Security Team\r\n\r\n| Name goes here | Name goes here |\r\n|--------------|-----------------|\r\n| Title goes here | Title goes here |\r\n| Email: Email@Email.com | Email: Email@Email.com |\r\n| Mobile: 555-555-5555 | Desk: 555-555-5555\t|\r\n\r\n"
            },
            "name": "text - 3"
          },
          {
            "type": 1,
            "content": {
              "json": "![Blank Space](https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Solid_white.svg/768px-Solid_white.svg.png)"
            },
            "customWidth": "10",
            "name": "text - 3"
          }
        ]
      },
      "customWidth": "100",
      "name": "group - 5"
    },
    {
      "type": 12,
      "content": {
        "version": "NotebookGroup/1.0",
        "groupType": "editable",
        "items": [
          {
            "type": 1,
            "content": {
              "json": "# Incidents Overview"
            },
            "name": "text - 8"
          },
          {
            "type": 3,
            "content": {
              "version": "KqlItem/1.0",
              "query": "// 1 month period not including this month\r\nlet StartofMonth = startofmonth(datetime(now), -1);\r\nlet EndofMonth = endofmonth(datetime(now), -1);\r\nSecurityIncident \r\n| where TimeGenerated between(StartofMonth ..(EndofMonth))\r\n| summarize arg_max(TimeGenerated, Status, Severity, Owner, AdditionalData,CreatedTime) by IncidentNumber\r\n| extend Tactics = todynamic(AdditionalData.tactics)\r\n| extend Owner = todynamic(Owner.assignedTo) \r\n| extend Product = todynamic((parse_json(tostring(AdditionalData.alertProductNames))[0])) \r\n| summarize count() by bin(CreatedTime, 1d)",
              "size": 1,
              "title": "Incidents Created Over Time",
              "queryType": 0,
              "resourceType": "microsoft.operationalinsights/workspaces",
              "visualization": "barchart"
            },
            "customWidth": "100",
            "name": "query - 3"
          },
          {
            "type": 3,
            "content": {
              "version": "KqlItem/1.0",
              "query": "// 1 month period not including this month\r\nlet StartofMonth = startofmonth(datetime(now), -1);\r\nlet EndofMonth = endofmonth(datetime(now), -1);\r\nSecurityIncident \r\n| where TimeGenerated between(StartofMonth ..(EndofMonth))\r\n| extend Tactics = todynamic(AdditionalData.tactics)\r\n| extend Owner = todynamic(Owner.assignedTo) \r\n| extend Product = todynamic((parse_json(tostring(AdditionalData.alertProductNames))[0])) \r\n| summarize Incidents=dcount(IncidentNumber) by Severity, bin(CreatedTime, 1d)",
              "size": 1,
              "title": "Incidents Created By Severity Over Time",
              "queryType": 0,
              "resourceType": "microsoft.operationalinsights/workspaces",
              "visualization": "unstackedbar"
            },
            "customWidth": "100",
            "name": "query - 11"
          },
          {
            "type": 3,
            "content": {
              "version": "KqlItem/1.0",
              "query": "// 1 month period not including this month\r\nlet StartofMonth = startofmonth(datetime(now), -1);\r\nlet EndofMonth = endofmonth(datetime(now), -1);\r\nSecurityIncident \r\n| where TimeGenerated between(StartofMonth ..(EndofMonth))\r\n| extend Tactics = todynamic(AdditionalData.tactics)\r\n| extend Owner = todynamic(Owner.assignedTo) \r\n| extend Product = todynamic((parse_json(tostring(AdditionalData.alertProductNames))[0])) \r\n| mvexpand Tactics to typeof(string)\r\n| summarize Incidents=dcount(IncidentNumber) by Tactics, bin(CreatedTime, 1d)",
              "size": 1,
              "title": "Incidents Created By Tactics Over Time",
              "queryType": 0,
              "resourceType": "microsoft.operationalinsights/workspaces",
              "visualization": "unstackedbar"
            },
            "customWidth": "100",
            "name": "query - 15"
          },
          {
            "type": 3,
            "content": {
              "version": "KqlItem/1.0",
              "query": "// 1 month period not including this month\r\nlet StartofMonth = startofmonth(datetime(now), -1);\r\nlet EndofMonth = endofmonth(datetime(now), -1);\r\nSecurityIncident\r\n| where TimeGenerated between(StartofMonth ..(EndofMonth))\r\n| extend Tactics = todynamic(AdditionalData.tactics)\r\n| extend Owner = todynamic(Owner.assignedTo) \r\n| extend Product = todynamic((parse_json(tostring(AdditionalData.alertProductNames))[0])) \r\n| summarize arg_max(TimeGenerated,*) by IncidentNumber \r\n| extend TimeToClosure =  (ClosedTime - CreatedTime)/1h\r\n| summarize 50th_Percentile=percentile(TimeToClosure, 50)",
              "size": 3,
              "title": "Mean Time To Closure",
              "queryType": 0,
              "resourceType": "microsoft.operationalinsights/workspaces",
              "visualization": "tiles",
              "tileSettings": {
                "titleContent": {
                  "formatter": 1
                },
                "leftContent": {
                  "columnMatch": "50th_Percentile",
                  "formatter": 12,
                  "formatOptions": {
                    "palette": "auto"
                  },
                  "numberFormat": {
                    "unit": 26,
                    "options": {
                      "style": "decimal",
                      "maximumFractionDigits": 3
                    }
                  }
                },
                "showBorder": false
              }
            },
            "customWidth": "50",
            "name": "query - 17"
          },
          {
            "type": 3,
            "content": {
              "version": "KqlItem/1.0",
              "query": "// 1 month period not including this month\r\nlet StartofMonth = startofmonth(datetime(now), -1);\r\nlet EndofMonth = endofmonth(datetime(now), -1);\r\nSecurityIncident\r\n| where TimeGenerated between(StartofMonth ..(EndofMonth))\r\n| extend Tactics = todynamic(AdditionalData.tactics)\r\n| extend Owner = todynamic(Owner.assignedTo) \r\n| extend Product = todynamic((parse_json(tostring(AdditionalData.alertProductNames))[0])) \r\n| summarize arg_max(LastModifiedTime,*) by IncidentNumber \r\n| extend TimeToClosure =  (ClosedTime - CreatedTime)/1h\r\n| summarize 5th_Percentile=percentile(TimeToClosure, 5),50th_Percentile=percentile(TimeToClosure, 50), 90th_Percentile=percentile(TimeToClosure, 90),99th_Percentile=percentile(TimeToClosure, 99) by bin(ClosedTime, 1d)\r\n",
              "size": 1,
              "title": "Time To Closure (Percentiles)",
              "queryType": 0,
              "resourceType": "microsoft.operationalinsights/workspaces",
              "visualization": "linechart"
            },
            "customWidth": "100",
            "name": "query - 13"
          },
          {
            "type": 3,
            "content": {
              "version": "KqlItem/1.0",
              "query": "// 1 month period not including this month\r\nlet StartofMonth = startofmonth(datetime(now), -1);\r\nlet EndofMonth = endofmonth(datetime(now), -1);\r\nSecurityIncident \r\n| where TimeGenerated between(StartofMonth ..(EndofMonth))\r\n| summarize arg_max(TimeGenerated,Status, Severity, Owner, AdditionalData) by IncidentNumber\r\n| extend Tactics = todynamic(AdditionalData.tactics)\r\n| extend Owner = todynamic(Owner.assignedTo) \r\n| extend Product = todynamic((parse_json(tostring(AdditionalData.alertProductNames))[0])) \r\n| summarize dcount(IncidentNumber) by Severity",
              "size": 1,
              "title": "Incidents Created By Severity",
              "queryType": 0,
              "resourceType": "microsoft.operationalinsights/workspaces",
              "visualization": "barchart"
            },
            "name": "query - 7",
            "styleSettings": {
              "margin": "5px",
              "padding": "5px"
            }
          },
          {
            "type": 3,
            "content": {
              "version": "KqlItem/1.0",
              "query": "// 1 month period not including this month\r\nlet StartofMonth = startofmonth(datetime(now), -1);\r\nlet EndofMonth = endofmonth(datetime(now), -1);\r\nSecurityIncident \r\n| where TimeGenerated between(StartofMonth ..(EndofMonth))\r\n| summarize arg_max(TimeGenerated, Status, Severity, Owner, AdditionalData,CreatedTime) by IncidentNumber, Title\r\n| extend Tactics = todynamic(AdditionalData.tactics)\r\n| extend Owner = todynamic(Owner.assignedTo) \r\n| extend Product = todynamic((parse_json(tostring(AdditionalData.alertProductNames))[0])) \r\n| summarize count() by bin(CreatedTime, 1h), Title\r\n| order by count_ desc",
              "size": 1,
              "title": "Incidents Created By Name",
              "queryType": 0,
              "resourceType": "microsoft.operationalinsights/workspaces",
              "visualization": "barchart"
            },
            "name": "query - 17",
            "styleSettings": {
              "margin": "5px",
              "padding": "5px"
            }
          },
          {
            "type": 1,
            "content": {
              "json": "![Blank Space](https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Solid_white.svg/768px-Solid_white.svg.png)"
            },
            "customWidth": "12",
            "name": "text - 10"
          },
          {
            "type": 3,
            "content": {
              "version": "KqlItem/1.0",
              "query": "// 1 month period not including this month\r\nlet StartofMonth = startofmonth(datetime(now), -1);\r\nlet EndofMonth = endofmonth(datetime(now), -1);\r\nSecurityIncident\r\n| where TimeGenerated between(StartofMonth ..(EndofMonth))\r\n| where Status == 'Closed'\r\n| extend Tactics = todynamic(AdditionalData.tactics)\r\n| extend Owner = todynamic(Owner.assignedTo) \r\n| extend Product = todynamic((parse_json(tostring(AdditionalData.alertProductNames))[0])) \r\n| extend feedback =strcat(Classification,\" \",ClassificationReason)\r\n| summarize dcount(IncidentNumber) by feedback\r\n",
              "size": 1,
              "title": "Incidents By Closing Classification",
              "queryType": 0,
              "resourceType": "microsoft.operationalinsights/workspaces",
              "visualization": "barchart"
            },
            "name": "query - 5",
            "styleSettings": {
              "margin": "5px",
              "padding": "5px"
            }
          }
        ]
      },
      "customWidth": "100",
      "name": "group - 16"
    },
    {
      "type": 12,
      "content": {
        "version": "NotebookGroup/1.0",
        "groupType": "editable",
        "items": [
          {
            "type": 1,
            "content": {
              "json": "# Alert Overview\r\n\r\n\r\n\r\n\r\n\r\n"
            },
            "name": "text - 0"
          },
          {
            "type": 3,
            "content": {
              "version": "KqlItem/1.0",
              "query": "// 1 month period not including this month\r\nlet StartofMonth = startofmonth(datetime(now), -1);\r\nlet EndofMonth = endofmonth(datetime(now), -1);\r\nAuditLogs\r\n| where TimeGenerated between(StartofMonth ..(EndofMonth))\r\n| extend initiatingUserPrincipalName = tostring(InitiatedBy.user.userPrincipalName)\r\n| where initiatingUserPrincipalName != \"\" \r\n| summarize Count = count() by Category\r\n| order by Count desc",
              "size": 3,
              "title": "Categories volume",
              "exportFieldName": "Category",
              "exportParameterName": "CategoryFIlter",
              "exportDefaultValue": "All",
              "queryType": 0,
              "resourceType": "microsoft.operationalinsights/workspaces",
              "visualization": "tiles",
              "tileSettings": {
                "titleContent": {
                  "columnMatch": "Category",
                  "formatter": 1,
                  "formatOptions": {
                    "showIcon": true
                  }
                },
                "leftContent": {
                  "columnMatch": "Count",
                  "formatter": 12,
                  "formatOptions": {
                    "palette": "auto",
                    "showIcon": true
                  },
                  "numberFormat": {
                    "unit": 17,
                    "options": {
                      "style": "decimal",
                      "maximumFractionDigits": 2,
                      "maximumSignificantDigits": 3
                    }
                  }
                },
                "secondaryContent": {
                  "columnMatch": "Trend",
                  "formatter": 21,
                  "formatOptions": {
                    "palette": "purple",
                    "showIcon": true
                  }
                },
                "showBorder": false
              }
            },
            "name": "query - 4"
          },
          {
            "type": 3,
            "content": {
              "version": "KqlItem/1.0",
              "query": "// 1 month period not including this month\r\nlet StartofMonth = startofmonth(datetime(now), -1);\r\nlet EndofMonth = endofmonth(datetime(now), -1);\r\nlet appData = AuditLogs\r\n| where TimeGenerated between(StartofMonth ..(EndofMonth))\r\n| summarize TotalCount = count() by OperationName, Category\r\n| join kind=inner (AuditLogs\r\n    | make-series Trend = count() default = 0 on TimeGenerated in range(now(-30d), now(-1m), 1h) by OperationName\r\n    | project-away TimeGenerated) on OperationName\r\n| order by TotalCount desc, OperationName asc\r\n| project OperationName, TotalCount, Trend, Category\r\n| serialize Id = row_number();\r\nAuditLogs\r\n| where TimeGenerated between(StartofMonth ..(EndofMonth))\r\n| extend initiator = iif (tostring(InitiatedBy.user.userPrincipalName) != \"\", tostring(InitiatedBy.user.userPrincipalName), \"unknown\")\r\n| summarize TotalCount = count() by initiator = iif (tostring(InitiatedBy.user.userPrincipalName) != \"\", tostring(InitiatedBy.user.userPrincipalName), \"unknown\"), Category, OperationName\r\n| join kind=inner (AuditLogs\r\n    | make-series Trend = count() default = 0 on TimeGenerated in range(now(-30d), now(-1m), 1h) by OperationName, initiator = iif (tostring(InitiatedBy.user.userPrincipalName) != \"\", tostring(InitiatedBy.user.userPrincipalName), \"unknown\")\r\n    | project-away TimeGenerated) on OperationName, initiator\r\n| order by TotalCount desc, OperationName asc\r\n| project OperationName, initiator, TotalCount, Category, Trend\r\n| serialize Id = row_number(1000000)\r\n| join kind=inner (appData) on OperationName\r\n| project Id, Name = initiator, Type = 'initiator', ['Operations Count'] = TotalCount, Trend, Category, ParentId = Id1\r\n| union (appData \r\n    | project Id, Name = OperationName, Type = 'Operation', ['Operations Count'] = TotalCount, Category, Trend)\r\n| where ['Operations Count'] != 0\r\n| order by ['Operations Count'] desc, Name asc\r\n| top 48 by  ['Operations Count']",
              "size": 3,
              "title": "User Activities",
              "exportParameterName": "UserInfo",
              "exportDefaultValue": "{ \"Name\":\"\", \"Type\":\"*\"}",
              "queryType": 0,
              "resourceType": "microsoft.operationalinsights/workspaces",
              "gridSettings": {
                "formatters": [
                  {
                    "columnMatch": "Id",
                    "formatter": 5
                  },
                  {
                    "columnMatch": "Name",
                    "formatter": 0,
                    "formatOptions": {
                      "customColumnWidthSetting": "45ch"
                    }
                  },
                  {
                    "columnMatch": "Type",
                    "formatter": 5
                  },
                  {
                    "columnMatch": "Operations Count",
                    "formatter": 8,
                    "formatOptions": {
                      "min": 0,
                      "palette": "blue",
                      "customColumnWidthSetting": "15ch"
                    },
                    "numberFormat": {
                      "unit": 0,
                      "options": {
                        "style": "decimal"
                      }
                    }
                  },
                  {
                    "columnMatch": "Trend",
                    "formatter": 9,
                    "formatOptions": {
                      "min": 0,
                      "palette": "turquoise",
                      "customColumnWidthSetting": "15ch"
                    },
                    "numberFormat": {
                      "unit": 0,
                      "options": {
                        "style": "decimal"
                      }
                    }
                  },
                  {
                    "columnMatch": "Category",
                    "formatter": 0,
                    "formatOptions": {
                      "customColumnWidthSetting": "25ch"
                    }
                  },
                  {
                    "columnMatch": "ParentId",
                    "formatter": 5
                  }
                ],
                "hierarchySettings": {
                  "idColumn": "Id",
                  "parentColumn": "ParentId",
                  "treeType": 0,
                  "expanderColumn": "Name"
                }
              }
            },
            "customWidth": "100",
            "showPin": false,
            "name": "query - 2"
          },
          {
            "type": 3,
            "content": {
              "version": "KqlItem/1.0",
              "query": "// 1 month period not including this month\r\nlet StartofMonth = startofmonth(datetime(now), -1);\r\nlet EndofMonth = endofmonth(datetime(now), -1);\r\nAuditLogs\r\n| where TimeGenerated between(StartofMonth ..(EndofMonth))\r\n| extend initiatingUserPrincipalName = iif (tostring(InitiatedBy.user.userPrincipalName) != \"\", tostring(InitiatedBy.user.userPrincipalName), \"unknown\")\r\n| where initiatingUserPrincipalName != \"\" \r\n| summarize Activities = count() by initiatingUserPrincipalName\r\n| sort by Activities desc nulls last ",
              "size": 3,
              "title": "Top Active Users",
              "queryType": 0,
              "resourceType": "microsoft.operationalinsights/workspaces",
              "visualization": "piechart"
            },
            "customWidth": "100",
            "name": "query - 3"
          }
        ]
      },
      "name": "group - 18"
    },
    {
      "type": 12,
      "content": {
        "version": "NotebookGroup/1.0",
        "groupType": "editable",
        "items": [
          {
            "type": 1,
            "content": {
              "json": "# Alerts Overview"
            },
            "name": "text - 0"
          },
          {
            "type": 3,
            "content": {
              "version": "KqlItem/1.0",
              "query": "// 1 month period not including this month\r\nlet StartofMonth = startofmonth(datetime(now), -1);\r\nlet EndofMonth = endofmonth(datetime(now), -1);\r\nSecurityAlert \r\n| where TimeGenerated between(StartofMonth ..(EndofMonth))\r\n| summarize count() by AlertName",
              "size": 1,
              "title": "Alert Trends",
              "queryType": 0,
              "resourceType": "microsoft.operationalinsights/workspaces",
              "visualization": "unstackedbar"
            },
            "name": "query - 2"
          },
          {
            "type": 3,
            "content": {
              "version": "KqlItem/1.0",
              "query": "// 1 month period not including this month\r\nlet StartofMonth = startofmonth(datetime(now), -3);\r\nlet EndofMonth = endofmonth(datetime(now), -1);\r\nSecurityAlert \r\n| where TimeGenerated between(StartofMonth ..(EndofMonth))\r\n| summarize count() by AlertSeverity",
              "size": 4,
              "title": "Alert Severity Distribution",
              "queryType": 0,
              "resourceType": "microsoft.operationalinsights/workspaces",
              "visualization": "unstackedbar"
            },
            "name": "query - 2 - Copy"
          },
          {
            "type": 3,
            "content": {
              "version": "KqlItem/1.0",
              "query": "// 1 month period not including this month\r\nlet StartofMonth = startofmonth(datetime(now), -1);\r\nlet EndofMonth = endofmonth(datetime(now), -1);\r\nSecurityAlert \r\n| where TimeGenerated between(StartofMonth ..(EndofMonth))\r\n| summarize count() by AlertName\r\n| top 10 by count_",
              "size": 3,
              "title": "Top 10 Alert Types",
              "queryType": 0,
              "resourceType": "microsoft.operationalinsights/workspaces",
              "visualization": "tiles",
              "tileSettings": {
                "showBorder": false,
                "titleContent": {
                  "columnMatch": "AlertName",
                  "formatter": 1
                },
                "leftContent": {
                  "columnMatch": "count_",
                  "formatter": 12,
                  "formatOptions": {
                    "palette": "auto"
                  },
                  "numberFormat": {
                    "unit": 17,
                    "options": {
                      "maximumSignificantDigits": 3,
                      "maximumFractionDigits": 2
                    }
                  }
                }
              }
            },
            "name": "query - 5"
          },
          {
            "type": 3,
            "content": {
              "version": "KqlItem/1.0",
              "query": "// 1 month period not including this month\r\nlet StartofMonth = startofmonth(datetime(now), -1);\r\nlet EndofMonth = endofmonth(datetime(now), -1);\r\nSecurityAlert \r\n| where TimeGenerated between(StartofMonth ..(EndofMonth))\r\n| extend Device = strcat(tostring(parse_json(ExtendedProperties)[\"DeviceId\"]))\r\n| summarize Total = count(), High = countif(AlertSeverity == \"High\"), Med = countif(AlertSeverity == \"Medium\"), Low = countif(AlertSeverity == \"Low\") by AlertName, Device\r\n| order by Total desc\r\n| top 20 by Total\r\n| project AlertName, Total, High, Med, Low",
              "size": 3,
              "title": "Alert Count",
              "queryType": 0,
              "resourceType": "microsoft.operationalinsights/workspaces",
              "tileSettings": {
                "showBorder": false,
                "titleContent": {
                  "columnMatch": "Device",
                  "formatter": 1
                },
                "leftContent": {
                  "columnMatch": "Total",
                  "formatter": 12,
                  "formatOptions": {
                    "palette": "auto"
                  },
                  "numberFormat": {
                    "unit": 17,
                    "options": {
                      "maximumSignificantDigits": 3,
                      "maximumFractionDigits": 2
                    }
                  }
                }
              },
              "graphSettings": {
                "type": 0,
                "topContent": {
                  "columnMatch": "Device",
                  "formatter": 1
                },
                "centerContent": {
                  "columnMatch": "Total",
                  "formatter": 1,
                  "numberFormat": {
                    "unit": 17,
                    "options": {
                      "maximumSignificantDigits": 3,
                      "maximumFractionDigits": 2
                    }
                  }
                }
              }
            },
            "name": "query - 9"
          },
          {
            "type": 3,
            "content": {
              "version": "KqlItem/1.0",
              "query": "// 1 month period not including this month\r\nlet StartofMonth = startofmonth(datetime(now), -1);\r\nlet EndofMonth = endofmonth(datetime(now), -1);\r\n//\r\nlet previousResults = SecurityAlert \r\n| where TimeGenerated between(StartofMonth ..(EndofMonth))\r\n| summarize P=count() by AlertName;\r\nlet currentResults =  SecurityAlert \r\n| where TimeGenerated between(StartofMonth ..(EndofMonth))\r\n| summarize C=count() by AlertName;\r\ncurrentResults | join kind=fullouter (\r\n    previousResults\r\n) on AlertName \r\n| extend Previous = iff(isnull(P),0,P)  \r\n| extend Current = iff(isnull(C),0,C) \r\n| extend Change = ((Current - Previous)/todouble(Previous))*100 \r\n| extend Alert=iff(AlertName == \"\",AlertName1,AlertName)\r\n| project-away AlertName1, AlertName, C, P \r\n| project Alert, Previous, Current, Change\r\n| order by Change",
              "size": 3,
              "title": "Alert Status",
              "queryType": 0,
              "resourceType": "microsoft.operationalinsights/workspaces"
            },
            "name": "query - 11"
          }
        ]
      },
      "name": "group - 17"
    },
    {
      "type": 12,
      "content": {
        "version": "NotebookGroup/1.0",
        "groupType": "editable",
        "items": [
          {
            "type": 1,
            "content": {
              "json": "![Blank Space](https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Solid_white.svg/768px-Solid_white.svg.png)"
            },
            "customWidth": "45",
            "name": "text - 7"
          },
          {
            "type": 1,
            "content": {
              "json": "# Security"
            },
            "name": "text - 0"
          },
          {
            "type": 3,
            "content": {
              "version": "KqlItem/1.0",
              "query": "// 1 month period not including this month\r\nlet StartofMonth = startofmonth(datetime(now), -1);\r\nlet EndofMonth = endofmonth(datetime(now), -1);\r\nlet scEvents = dynamic([5827, 5828, 5829, 5830, 5831]);\r\nlet legacyAuth = SigninLogs\r\n| where TimeGenerated between(StartofMonth ..(EndofMonth))\r\n| where ResultType == 0\r\n| where ClientAppUsed !contains \"Browser\" and ClientAppUsed !contains \"Mobile Apps and Desktop clients\"\r\n| summarize Count=count() by Protocol=\"AAD Legacy Auth\";\r\nSecurityEvent\r\n| where TimeGenerated between(StartofMonth ..(EndofMonth))\r\n| parse EventData with * '\"TicketEncryptionType\">' TicketEncryptionType '<' *\r\n| union Event\r\n| where (EventID == 2889) or (EventID == 3000 and EventLog == 'Microsoft-Windows-SMBServer/Audit') or (EventID == 4624 and AuthenticationPackageName == 'NTLM' and LmPackageName == 'NTLM V1' and Account !contains 'ANONYMOUS LOGON') or ((EventID == 4624 or EventID == 4776) and Level == 8 and PackageName contains 'WDigest') or (EventID == 4768 or EventID == 4769) and Level == 8 and (TicketEncryptionType != \"0x12\" and TicketEncryptionType != \"0x11\") or ((EventLog =~ \"System\" and Source =~ \"NETLOGON\") and EventID in (scEvents))\r\n| summarize Count=count() by bin(TimeGenerated, 1d), tostring(EventID)\r\n//| extend Protocol=replace(tostring(4776), 'WDigest', replace(tostring(4768), 'Kerberos weak cipher', replace(tostring(4769), 'Kerberos weak cipher', replace(tostring(2889), 'Insecure LDAP', replace(tostring(4624), 'NTLM v1', replace(tostring(3000), 'SMB v1', tostring(EventID)))))))\r\n| extend Protocol = case(EventID == 4776, \"WDigest\", EventID == 4768 or EventID == 4769, \"Weak Kerberos Cipher\", EventID == 2889, \"Insecure LDAP\", EventID == 4624, \"NTLM v1\", EventID == 3000, \"SMBv1\", EventID in (scEvents), \"Vulnerable Secure Channel\", \"Unknown\")\r\n| project Protocol, Count\r\n| union legacyAuth\r\n| sort by Count desc",
              "size": 3,
              "title": "Summary of Insecure Protocols",
              "noDataMessage": "No Insecure Protocols Found During This Time Period",
              "queryType": 0,
              "resourceType": "microsoft.operationalinsights/workspaces",
              "visualization": "piechart"
            },
            "name": "query - 7"
          },
          {
            "type": 3,
            "content": {
              "version": "KqlItem/1.0",
              "query": "// 1 month period not including this month\r\nlet StartofMonth = startofmonth(datetime(now), -1);\r\nlet EndofMonth = endofmonth(datetime(now), -1);\r\nlet scEvents = dynamic([5827, 5828, 5829, 5830, 5831]);\r\nlet legacyAuth = SigninLogs\r\n| where TimeGenerated between(StartofMonth ..(EndofMonth))\r\n| where ResultType == 0\r\n| where ClientAppUsed !contains \"Browser\" and ClientAppUsed !contains \"Mobile Apps and Desktop clients\"\r\n| summarize Count=count() by bin(TimeGenerated, 1d), Protocol=\"AAD Legacy Auth\";\r\nSecurityEvent\r\n| where TimeGenerated between(StartofMonth ..(EndofMonth))\r\n| parse EventData with * '\"TicketEncryptionType\">' TicketEncryptionType '<' *\r\n| union Event\r\n| where (EventID == 2889) or (EventID == 3000 and EventLog == 'Microsoft-Windows-SMBServer/Audit') or (EventID == 4624 and AuthenticationPackageName == 'NTLM' and LmPackageName == 'NTLM V1' and Account !contains 'ANONYMOUS LOGON') or ((EventID == 4624 or EventID == 4776) and Level == 8 and PackageName contains 'WDigest') or (EventID == 4768 or EventID == 4769) and Level == 8 and (TicketEncryptionType != \"0x12\" and TicketEncryptionType != \"0x11\") or ((EventLog =~ \"System\" and Source =~ \"NETLOGON\") and EventID in (scEvents))\r\n| summarize Count=count() by bin(TimeGenerated, 1d), tostring(EventID)\r\n//| extend Protocol=replace(tostring(4776), 'WDigest', replace(tostring(4768), 'Kerberos weak cipher', replace(tostring(4769), 'Kerberos weak cipher', replace(tostring(2889), 'Insecure LDAP', replace(tostring(4624), 'NTLM v1', replace(tostring(3000), 'SMB v1', tostring(EventID)))))))\r\n| extend Protocol = case(EventID == 4776, \"WDigest\", EventID == 4768 or EventID == 4769, \"Weak Kerberos Cipher\", EventID == 2889, \"Insecure LDAP\", EventID == 4624, \"NTLM v1\", EventID == 3000, \"SMBv1\", EventID in (scEvents), \"Vulnerable Secure Channel\", \"Unknown\")\r\n| project Protocol, Count, TimeGenerated\r\n| union legacyAuth\r\n| sort by Count desc",
              "size": 1,
              "title": "Summary of Insecure Protocols",
              "noDataMessage": "No Insecure Protocols Found During This Time Period",
              "queryType": 0,
              "resourceType": "microsoft.operationalinsights/workspaces",
              "visualization": "barchart"
            },
            "name": "query - 10"
          },
          {
            "type": 3,
            "content": {
              "version": "KqlItem/1.0",
              "query": "// 1 month period not including this month\r\nlet StartofMonth = startofmonth(datetime(now), -1);\r\nlet EndofMonth = endofmonth(datetime(now), -1);\r\nlet scEvents = dynamic([5827, 5828, 5829, 5830, 5831]);\r\nlet legacyAuth = SigninLogs\r\n| where TimeGenerated between(StartofMonth ..(EndofMonth))\r\n| where ResultType == 0\r\n| where ClientAppUsed !contains \"Browser\" and ClientAppUsed !contains \"Mobile Apps and Desktop clients\"\r\n| summarize FirstOccurance=min(TimeGenerated), LastOccurance=max(TimeGenerated), Count=count() by Protocol=\"AAD Legacy Auth\";\r\nSecurityEvent\r\n| where TimeGenerated between(StartofMonth ..(EndofMonth))\r\n| parse EventData with * '\"TicketEncryptionType\">' TicketEncryptionType '<' *\r\n| union Event\r\n| where (EventID == 2889) or (EventID == 3000 and EventLog == 'Microsoft-Windows-SMBServer/Audit') or (EventID == 4624 and AuthenticationPackageName == 'NTLM' and LmPackageName == 'NTLM V1' and Account !contains 'ANONYMOUS LOGON') or ((EventID == 4624 or EventID == 4776) and Level == 8 and PackageName contains 'WDigest') or (EventID == 4768 or EventID == 4769) and Level == 8 and (TicketEncryptionType != \"0x12\" and TicketEncryptionType != \"0x11\") or ((EventLog =~ \"System\" and Source =~ \"NETLOGON\") and EventID in (scEvents))\r\n| summarize FirstOccurance=min(TimeGenerated), LastOccurance=max(TimeGenerated), Count=count() by tostring(EventID)\r\n//| extend Protocol=replace(tostring(4776), 'WDigest', replace(tostring(4768), 'Kerberos weak cipher', replace(tostring(4769), 'Kerberos weak cipher', replace(tostring(2889), 'Insecure LDAP', replace(tostring(4624), 'NTLM v1', replace(tostring(3000), 'SMB v1', tostring(EventID)))))))\r\n| extend Protocol = case(EventID == 4776, \"WDigest\", EventID == 4768 or EventID == 4769, \"Weak Kerberos Cipher\", EventID == 2889, \"Insecure LDAP\", EventID == 4624, \"NTLM v1\", EventID == 3000, \"SMBv1\", EventID in (scEvents), \"Vulnerable Secure Channel\", \"Unknown\")\r\n| summarize FirstOccurance=min(FirstOccurance), LastOccurance=max(LastOccurance), Count=sum(Count) by Protocol\r\n| union legacyAuth\r\n| sort by Count desc",
              "size": 3,
              "title": "Summary of Insecure Protocols found",
              "noDataMessage": "No Insecure Protocols Found During This Time Period",
              "queryType": 0,
              "resourceType": "microsoft.operationalinsights/workspaces",
              "visualization": "table"
            },
            "name": "query - 11"
          },
          {
            "type": 3,
            "content": {
              "version": "KqlItem/1.0",
              "query": "// 1 month period not including this month\r\nlet StartofMonth = startofmonth(datetime(now), -1);\r\nlet EndofMonth = endofmonth(datetime(now), -1);\r\nSecurityEvent\r\n| where TimeGenerated between(StartofMonth ..(EndofMonth))\r\n| where EventID == \"4720\"\r\n| project TimeGenerated, Account=(AccountType), AdminAccount=(SubjectAccount), Computer",
              "size": 3,
              "title": "4720: A user account was created",
              "noDataMessage": "No User Accounts Were Created During This Time Period",
              "queryType": 0,
              "resourceType": "microsoft.operationalinsights/workspaces",
              "gridSettings": {
                "formatters": [
                  {
                    "columnMatch": "TimeGenerated",
                    "formatter": 0,
                    "formatOptions": {
                      "customColumnWidthSetting": "20ch"
                    }
                  },
                  {
                    "columnMatch": "Account",
                    "formatter": 0,
                    "formatOptions": {
                      "customColumnWidthSetting": "12ch"
                    }
                  },
                  {
                    "columnMatch": "AdminAccount",
                    "formatter": 0,
                    "formatOptions": {
                      "customColumnWidthSetting": "25ch"
                    }
                  },
                  {
                    "columnMatch": "Computer",
                    "formatter": 0,
                    "formatOptions": {
                      "customColumnWidthSetting": "45ch"
                    }
                  }
                ]
              }
            },
            "name": "query - 4"
          },
          {
            "type": 3,
            "content": {
              "version": "KqlItem/1.0",
              "query": "// 1 month period not including this month\r\nlet StartofMonth = startofmonth(datetime(now), -1);\r\nlet EndofMonth = endofmonth(datetime(now), -1);\r\nSecurityEvent\r\n| where TimeGenerated between(StartofMonth ..(EndofMonth))\r\n| where EventID == \"4738\"\r\n| where AccountType != \"Machine\"\r\n| project TimeGenerated, Admin=(SubjectAccount), Computer, TargetUser=(TargetUserName), PasswordLastSet\r\n| take 250",
              "size": 3,
              "title": "4738: A user account was changed",
              "noDataMessage": "No User Accounts Were Changed During This Time Period",
              "queryType": 0,
              "resourceType": "microsoft.operationalinsights/workspaces",
              "gridSettings": {
                "formatters": [
                  {
                    "columnMatch": "TimeGenerated",
                    "formatter": 0,
                    "formatOptions": {
                      "customColumnWidthSetting": "20ch"
                    }
                  },
                  {
                    "columnMatch": "Admin",
                    "formatter": 0,
                    "formatOptions": {
                      "customColumnWidthSetting": "25ch"
                    }
                  },
                  {
                    "columnMatch": "Computer",
                    "formatter": 0,
                    "formatOptions": {
                      "customColumnWidthSetting": "30ch"
                    }
                  },
                  {
                    "columnMatch": "TargetUser",
                    "formatter": 0,
                    "formatOptions": {
                      "customColumnWidthSetting": "10ch"
                    }
                  },
                  {
                    "columnMatch": "PasswordLastSet",
                    "formatter": 0,
                    "formatOptions": {
                      "customColumnWidthSetting": "13ch"
                    }
                  },
                  {
                    "columnMatch": "AdminAccount",
                    "formatter": 0,
                    "formatOptions": {
                      "customColumnWidthSetting": "28ch"
                    }
                  }
                ]
              }
            },
            "name": "query - 5"
          },
          {
            "type": 1,
            "content": {
              "json": "![Blank Space](https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Solid_white.svg/768px-Solid_white.svg.png)"
            },
            "customWidth": "10",
            "name": "text - 8"
          },
          {
            "type": 3,
            "content": {
              "version": "KqlItem/1.0",
              "query": "// 1 month period not including this month\r\nlet StartofMonth = startofmonth(datetime(now), -1);\r\nlet EndofMonth = endofmonth(datetime(now), -1);\r\n// Logons With Clear Text Password \r\n// Logons with clear text password by target account. \r\nSecurityEvent\r\n| where TimeGenerated between(StartofMonth ..(EndofMonth))\r\n| where EventID == 4624 and LogonType == 8\r\n| summarize count() by TargetAccount",
              "size": 3,
              "title": "Logons With Clear Text Password",
              "noDataMessage": "Congratulations! No One Has Used Clear Text Passwords During this Time Period. ",
              "queryType": 0,
              "resourceType": "microsoft.operationalinsights/workspaces"
            },
            "name": "query - 6"
          }
        ]
      },
      "name": "group - 4"
    },
    {
      "type": 12,
      "content": {
        "version": "NotebookGroup/1.0",
        "groupType": "editable",
        "items": [
          {
            "type": 1,
            "content": {
              "json": "# Billable"
            },
            "name": "text - 0"
          },
          {
            "type": 3,
            "content": {
              "version": "KqlItem/1.0",
              "query": "//BILLABLE USAGE:\r\nlet StartofMonth = startofmonth(datetime(now), -1);\r\nlet EndofMonth = endofmonth(datetime(now), -1);\r\nUsage\r\n| where TimeGenerated between(StartofMonth ..(EndofMonth))\r\n| where IsBillable\r\n| summarize DataGB = sum(Quantity / 1000.) by Date = bin(TimeGenerated, 1d)\r\n| sort by Date desc",
              "size": 1,
              "title": "Billable Usage",
              "queryType": 0,
              "resourceType": "microsoft.operationalinsights/workspaces",
              "visualization": "barchart"
            },
            "name": "query - 1"
          }
        ]
      },
      "name": "group - 7"
    },
    {
      "type": 12,
      "content": {
        "version": "NotebookGroup/1.0",
        "groupType": "editable",
        "items": [
          {
            "type": 1,
            "content": {
              "json": "# Security Contacts\r\n## Service-Now Portal Users\r\nTo Obtain a Web Portal Login:\r\n1. Go to https://datalink.service-now.com\r\n2. Click the self-registration form link\r\n3. Complete and submit the User Registration Request form\r\n4. You will receive an email with your new login credentials"
            },
            "customWidth": "100",
            "name": "text - 0"
          },
          {
            "type": 1,
            "content": {
              "json": "#  \r\n#  \r\n#   \r\n#  \r\n#  \r\n#  \r\n#  \r\n#  \r\n#  "
            },
            "name": "text - 3"
          },
          {
            "type": 1,
            "content": {
              "json": "#  \r\n# Getting Support \r\n## How to Contact Company Support\r\n| Case Priority | Action | Contact info |\r\n|---------------|--------|--------------|\r\n| P1 | Call Support for Immediate Response| |\r\n|P2-P4| Email | Email@Email.com |\r\n|P2-P4| Email | Email@Email.com |\r\n|P2-P4| Portal | https://Customer.portal |\r\n|P2-P4| Phone | 555-555-5555 |\r\n\r\n"
            },
            "customWidth": "100",
            "name": "text - 1"
          },
          {
            "type": 1,
            "content": {
              "json": "## Service Level Parameters\r\n| Priority Setting | Initial Response | SLA Measure | Service Resolution | Update Case |\r\n|------------------|------------------|-------------|--------------------|-------------|\r\n| 1 | 60 Minutes | Incident Response Time | 4 Hours | 1 Hour |\r\n| 2 | 2 Hours | Incident Response Time | 6 Hours | 2 Hours |\r\n| 3 | 4 Hours | Incident Response Time | 5 Days | 24 Hours |\r\n| 4 | 72 Hours | Incident Response Time | N/A | 72 Hours |\r\n\r\n\r\n## Definitions of Priority Levels\r\n**Critical (Priority 1):** Your system is inoperable or is at a severely reduced level of functionality. Adverse impact on normal business operations – no immediate resolution available\r\n\r\n**Severe (Priority 2):** Intermittent failures or performance degradation that has limited normal business operations\r\n\r\n**Medium (Priority 3):** Conditions are defined as a minor incident that can be worked around without major impact to your normal business \r\n\r\n**Low (Priority 4):** General questions or a minor incident that has little to no impact on your normal business operations\r\n\r\n\r\n## Escalation Process & Contacts\r\nCall 555-555-5555 (SOC) or 555-555-5555 and ask for the NOC Duty Manager on-call; or,\r\n\r\nIf further escalation is required, please follow the contact chain below:\r\n - Contact the <Title here>  - Name (Email@Email.com Phone: 555-555-5555)\r\n - Contact the <Title here> - Name (Email@Email.com)"
            },
            "name": "text - 2"
          }
        ]
      },
      "name": "group - 4"
    }
  ],
  "fallbackResourceIds": [
    "<resources>"
  ],
  "fromTemplateId": "sentinel-UserWorkbook",
  "$schema": "<resources>"
}
```
