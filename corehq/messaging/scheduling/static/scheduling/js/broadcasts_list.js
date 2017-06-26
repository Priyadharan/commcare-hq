hqDefine("scheduling/js/broadcasts_list.js", function() {
    $(function() {
        var immediate_table,
            scheduled_table,
            list_broadcasts_url = hqImport("hqwebapp/js/urllib.js").reverse("new_list_broadcasts"),
            loader_src = hqImport("hqwebapp/js/initial_page_data.js").get("loader_src");

        scheduled_table = $("#scheduled-table").dataTable({
            "lengthChange": false,
            "filter": false,
            "sort": false,
            "displayLength": 5,
            "processing": true,
            "serverSide": true,
            "ajaxSource": list_broadcasts_url,
            "fnServerParams": function(aoData) {
                aoData.push({"name": "action", "value": "list_scheduled"});
            },
            "sDom": "rtp",
            "language": {
                "emptyTable": gettext('There are no messages to display.'),
                "infoEmpty": gettext('There are no messages to display.'),
                "lengthMenu": gettext('Show _MENU_ messages per page'),
                "processing": '<img src="' + loader_src + '" /> ' + gettext('Loading messages...'),
                "info": gettext('Showing _START_ to _END_ of _TOTAL_ broadcasts'),
                "infoFiltered": gettext('(filtered from _MAX_ total broadcasts)'),
            },
            "columnDefs": [
                {
                    "targets": [0],
                    "render": function() {
                        // TODO construct this from ID
                        return 'Delete button';
                    },
                },
                {
                    "targets": [1],
                    "render": function(data) {
                        // TODO link this to the view
                        return data;
                    },
                },
                {
                    "targets": [3],
                    "render": function(data) {
                        return data ? gettext("Active") : gettext("Inactive");
                    },
                },
                {
                    "targets": [4],
                    "render": function() {
                        // TODO construct this from ID
                        return 'activate or deactivate button';
                    },
                },
            ],
        });
        immediate_table = $("#immediate-table").dataTable({
            "lengthChange": false,
            "filter": false,
            "sort": false,
            "displayLength": 5,
            "processing": true,
            "serverSide": true,
            "ajaxSource": list_broadcasts_url,
            "fnServerParams": function(aoData) {
                aoData.push({"name": "action", "value": "list_immediate"});
            },
            "dom": "rtp",
            "language": {
                "emptyTable": gettext('There are no messages to display.'),
                "infoEmpty": gettext('There are no messages to display.'),
                "lengthMenu": gettext('Show _MENU_ messages per page'),
                "processing": '<img src="' + loader_src + '" /> ' + gettext('Loading Messages...'),
                "info": gettext('Showing _START_ to _END_ of _TOTAL_ messages'),
                "infoFiltered": gettext('(filtered from _MAX_ total messages)'),
            },
            "columnDefs": [
                {
                    "targets": [0],
                    "render": function(data) {
                        // TODO link this to the view
                        return data;
                    },
                },
            ],
        });
    });
});
