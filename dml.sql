SELECT * FROM lol_insights.lol_data.challengers;

UPDATE lol_insights.lol_data.servers_info
SET server_routing_value = REPLACE(server_routing_value,'KR1','KR');

UPDATE lol_insights.lol_data.servers_info
SET server_routing_value = REPLACE(server_routing_value,'RU1','RU');

SELECT DISTINCT server_routing_value FROM lol_insights.lol_data.servers_info;
