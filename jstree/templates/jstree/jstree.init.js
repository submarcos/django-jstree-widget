<script type="text/javascript">
    $(document).ready(function() {
        $('#{{ div_id }}').jstree({
            'core' : {
                'data' : {
                    'url' : "{{ url }}",
                    'data' : function (node) {
                      return { 'id' : node.id };
                    }
                },
                'themes': {
                    'name': 'proton',
                    'responsive': true
                }
            }
        });

        $('#{{ div_id }}').on(
            "select_node.jstree",
            function (e, data) {
                $('#id_{{ field_name }}').val(data.node.id);
            }
        );
    });
</script>