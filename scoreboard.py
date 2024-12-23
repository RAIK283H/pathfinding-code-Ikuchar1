import math
import pyglet
import colors
import config_data
import global_game_data
import graph_data


class Scoreboard:
    player_name_display = []
    player_traveled_display = []
    player_excess_distance_display = []
    player_path_display = []
    player_nodes_visited_display = []
    winning_player_display = []

    def __init__(self, batch, group):
        self.batch = batch
        self.group = group
        self.stat_height = 32
        self.stat_width = 400
        self.number_of_stats = 5
        self.base_height_offset = 20
        self.font_size = 16
        self.distance_to_exit_label = pyglet.text.Label('Direct Distance To Exit : 0', x=0, y=0,
                                                        font_name='Arial', font_size=self.font_size, batch=batch, group=group)
        self.distance_to_exit = 0
        for index, player in enumerate(config_data.player_data):
            player_name_label = pyglet.text.Label(str(index + 1) + " " + player[0],
                                                  x=0,
                                                  y=0,
                                                  font_name='Arial',
                                                  font_size=self.font_size, batch=batch, group=group, color=player[2][colors.TEXT_INDEX])
            self.player_name_display.append((player_name_label, player))
            traveled_distance_label = pyglet.text.Label("Distance Traveled:",
                                                        x=0,
                                                        y=0,
                                                        font_name='Arial',
                                                        font_size=self.font_size, batch=batch, group=group, color=player[2][colors.TEXT_INDEX])
            self.player_traveled_display.append(
                (traveled_distance_label, player))
            excess_distance_label = pyglet.text.Label("Excess Distance Traveled:",
                                                      x=0,
                                                      y=0,
                                                      font_name='Arial',
                                                      font_size=self.font_size, batch=batch, group=group, color=player[2][colors.TEXT_INDEX])

            self.player_excess_distance_display.append(
                (excess_distance_label, player))
            
            path_label = pyglet.text.Label("",
                                   x=0,
                                   y=0,
                                   font_name='Arial',
                                   font_size=self.font_size, batch=batch, group=group, color=player[2][colors.TEXT_INDEX])
            self.player_path_display.append(
                (path_label, player))
            
            nodes_visited_label = pyglet.text.Label("Nodes Visited: 0",
                                                    x=0,
                                                    y=0,
                                                    font_name='Arial',
                                                    font_size=self.font_size, batch=batch, group=group, color=player[2][colors.TEXT_INDEX])
            self.player_nodes_visited_display.append((nodes_visited_label,player))
            
            winner_label = pyglet.text.Label("Finding winner...",
                                            x = 0,
                                            y = 0,
                                            font_name = "Arial",
                                            font_size=self.font_size, batch=batch, group=group)
            self.winning_player_display = (winner_label, player)
            


    def update_elements_locations(self):
        self.distance_to_exit_label.x = config_data.window_width - self.stat_width
        self.distance_to_exit_label.y = config_data.window_height - self.stat_height
        #display_element = self.winning_player_display[0]
        #winner_label = self.winning_player_display[0]
        #winner_label.x = config_data.window_width - self.stat_width
        #winner_label.y = config_data.window_height - self.stat_height * 15
        for index, (display_element, player) in enumerate(self.player_name_display):
            display_element.x = config_data.window_width - self.stat_width
            display_element.y = config_data.window_height - self.base_height_offset - self.stat_height * 2 - self.stat_height * (index * self.number_of_stats)
        for index, (display_element, player) in enumerate(self.player_traveled_display):
            display_element.x = config_data.window_width - self.stat_width
            display_element.y = config_data.window_height - self.base_height_offset - self.stat_height * 3 - self.stat_height * (index * self.number_of_stats)
        for index, (display_element, player) in enumerate(self.player_excess_distance_display):
            display_element.x = config_data.window_width - self.stat_width
            display_element.y = config_data.window_height - self.base_height_offset - self.stat_height * 4 - self.stat_height * (index * self.number_of_stats)
        for index, (display_element, player) in enumerate(self.player_path_display):
            display_element.x = config_data.window_width - self.stat_width
            display_element.y = config_data.window_height - self.base_height_offset - self.stat_height * 5 - self.stat_height * (index * self.number_of_stats)
        for index, (display_element, player) in enumerate(self.player_nodes_visited_display):
            display_element.x = config_data.window_width - self.stat_width
            display_element.y = config_data.window_height - self.base_height_offset - self.stat_height * 6 - self.stat_height * (index * self.number_of_stats)
        
        winner_label = self.winning_player_display[0]
        winner_label.x = config_data.window_width - self.stat_width * 2.2
        winner_label.y = config_data.window_height - self.stat_height * 26
        


    def update_paths(self):
        for index in range(len(config_data.player_data)):
            self.player_path_display[index][0].text = self.wrap_text(str(global_game_data.graph_paths[index]))

    def update_distance_to_exit(self):
        start_x = graph_data.graph_data[global_game_data.current_graph_index][0][0][0]
        start_y = graph_data.graph_data[global_game_data.current_graph_index][0][0][1]
        end_x = graph_data.graph_data[global_game_data.current_graph_index][-1][0][0]
        end_y = graph_data.graph_data[global_game_data.current_graph_index][-1][0][1]
        self.distance_to_exit = math.sqrt(pow(start_x - end_x, 2) + pow(start_y - end_y, 2))
        self.distance_to_exit_label.text = 'Direct Distance To Exit : ' + "{0:.0f}".format(self.distance_to_exit)

    def wrap_text(self, input):
        wrapped_text = (input[:44] + ', ...]') if len(input) > 44 else input
        return wrapped_text

    def update_distance_traveled(self):
        for display_element, player_configuration_info in self.player_traveled_display:
            for player_object in global_game_data.player_objects:
                if player_object.player_config_data == player_configuration_info:
                    display_element.text = "Distance Traveled: " + str(int(player_object.distance_traveled))

        for display_element, player_configuration_info in self.player_excess_distance_display:
            for player_object in global_game_data.player_objects:
                if player_object.player_config_data == player_configuration_info:
                    display_element.text = "Excess Distance Traveled: " + str(max(0, int(player_object.distance_traveled-self.distance_to_exit)))
                    
    def update_num_nodes_visited(self):
        for index in range(len(config_data.player_data)):
            self.player_nodes_visited_display[index][0].text = self.wrap_text("# Nodes Visited: " + str(len(global_game_data.graph_paths[index])))
            
    def update_winner(self):
        #looks thru all player stats and finds and displays winner
        graph_index = global_game_data.current_graph_index
        graph = graph_data.graph_data[graph_index]
        targetNode = global_game_data.target_node[global_game_data.current_graph_index]
        exitNode = len(graph) - 1
        displayElement = self.winning_player_display[0]
        
        curr_shortest_dist = global_game_data.player_objects[0].distance_traveled
        winner = config_data.player_data[0][0]
        
        for i, player in enumerate(global_game_data.player_objects):
            player_dist_traveled = player.distance_traveled
            path = global_game_data.graph_paths[i]
            is_Target_In_Path = targetNode in path
            is_Exit_In_Path = exitNode in path
            
            #update winner
            if(is_Target_In_Path and is_Exit_In_Path and (player_dist_traveled < curr_shortest_dist)):
                curr_shortest_dist = player_dist_traveled
                winner = config_data.player_data[i][0]

        #display the winner
        displayElement.text = "Winner: " + str(winner)
        
    #helper to reset winner text to right text when there is new graph
    def reset_winner_text(self):
        winner_label = self.winning_player_display[0]
        winner_label.text = "Finding winner..."
        
    def update_scoreboard(self):
        self.update_elements_locations()
        self.update_paths()
        self.update_distance_to_exit()
        self.update_distance_traveled()
        self.update_num_nodes_visited()
        #only update when it is on the last player.
        if (global_game_data.current_player_index == len(global_game_data.player_objects) - 1):
            self.update_winner()
