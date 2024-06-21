import javafx.application.Application;
import javafx.application.Platform;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.TextArea;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.stage.Stage;

import java.util.Random;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

public class FMSDisplay extends Application {

    private final Random random = new Random();

    private TextArea navDataTextArea;
    private TextArea perfDataTextArea;
    private TextArea weatherDataTextArea;
    private TextArea trafficDataTextArea;

    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("Flight Management System (FMS)");
        primaryStage.setWidth(1200);
        primaryStage.setHeight(800);

        GridPane grid = createGridPane();

        Scene scene = new Scene(grid, Color.BLACK);
        primaryStage.setScene(scene);
        primaryStage.show();

        updateData();
    }

    private GridPane createGridPane() {
        GridPane grid = new GridPane();
        grid.setPadding(new Insets(10));
        grid.setHgap(10);
        grid.setVgap(10);
        grid.setStyle("-fx-background-color: black;");

        // Navigation Frame
        VBox navigationFrame = createFrame();
        Label navigationLabel = createLabel("Navigation Data", "white");
        navDataTextArea = createTextArea();
        ScrollPane navScrollPane = new ScrollPane(navDataTextArea);
        navScrollPane.setFitToWidth(true);
        navigationFrame.getChildren().addAll(navigationLabel, navScrollPane);
        grid.add(navigationFrame, 0, 0);

        // Performance Frame
        VBox performanceFrame = createFrame();
        Label performanceLabel = createLabel("Performance Data", "white");
        perfDataTextArea = createTextArea();
        ScrollPane perfScrollPane = new ScrollPane(perfDataTextArea);
        perfScrollPane.setFitToWidth(true);
        performanceFrame.getChildren().addAll(performanceLabel, perfScrollPane);
        grid.add(performanceFrame, 1, 0);

        // Weather Frame
        VBox weatherFrame = createFrame();
        Label weatherLabel = createLabel("Weather Data", "white");
        weatherDataTextArea = createTextArea();
        ScrollPane weatherScrollPane = new ScrollPane(weatherDataTextArea);
        weatherScrollPane.setFitToWidth(true);
        weatherFrame.getChildren().addAll(weatherLabel, weatherScrollPane);
        grid.add(weatherFrame, 0, 1);

        // Traffic Frame
        VBox trafficFrame = createFrame();
        Label trafficLabel = createLabel("Traffic Information", "white");
        trafficDataTextArea = createTextArea();
        ScrollPane trafficScrollPane = new ScrollPane(trafficDataTextArea);
        trafficScrollPane.setFitToWidth(true);
        trafficFrame.getChildren().addAll(trafficLabel, trafficScrollPane);
        grid.add(trafficFrame, 1, 1);

        // Adding initial data
        initNavigationData();
        initPerformanceData();
        initWeatherData();
        initTrafficData();

        return grid;
    }

    private VBox createFrame() {
        VBox frame = new VBox(10);
        frame.setPadding(new Insets(10));
        frame.setStyle("-fx-border-color: gray; -fx-border-width: 2; -fx-background-color: black;");
        return frame;
    }

    private Label createLabel(String text, String color) {
        Label label = new Label(text);
        label.setTextFill(Color.web(color));
        label.setFont(Font.font("Helvetica", 20));
        return label;
    }

    private TextArea createTextArea() {
        TextArea textArea = new TextArea();
        textArea.setWrapText(false);
        textArea.setStyle("-fx-control-inner-background: black; -fx-text-fill: white; -fx-font-family: 'Helvetica'; -fx-font-size: 14;");
        textArea.setEditable(false);
        return textArea;
    }

    private void initNavigationData() {
        String navData = "Current Position: LAT 37.7749° N, LONG 122.4194° W\n" +
                         "Next Waypoint: WAYPOINT2\n" +
                         "Distance to Next Waypoint: 150 NM\n" +
                         "Estimated Time of Arrival: 12:34 UTC";
        navDataTextArea.setText(navData);
    }

    private void initPerformanceData() {
        String perfData = "Current Airspeed: 450 knots\n" +
                          "Current Altitude: 35,000 ft\n" +
                          "Fuel Remaining: 12,000 lbs\n" +
                          "Estimated Fuel at Destination: 6,500 lbs\n" +
                          "Gross Weight: 150,000 lbs\n" +
                          "Temperature: -40°C";
        perfDataTextArea.setText(perfData);
    }

    private void initWeatherData() {
        String weatherData = "Current Weather: Clear\n" +
                             "Wind: 270° at 15 knots\n" +
                             "Temperature: 20°C\n" +
                             "Visibility: 10 miles";
        weatherDataTextArea.setText(weatherData);
    }

    private void initTrafficData() {
        String trafficData = "Traffic: No Conflict\n" +
                             "Nearest Aircraft: 5 NM\n" +
                             "TCAS Status: Normal";
        trafficDataTextArea.setText(trafficData);
    }

    private void updateData() {
        ScheduledExecutorService executor = Executors.newScheduledThreadPool(1);
        executor.scheduleAtFixedRate(() -> {
            Platform.runLater(() -> {
                // Simulate dynamic data updates
                int newSpeed = random.nextInt(21) + 440;
                int newAltitude = random.nextInt(2001) + 34000;
                int newFuel = random.nextInt(1001) + 11500;
                String navPosition = String.format("Current Position: LAT %.4f° N, LONG %.4f° W",
                        random.nextDouble() * 20 + 30, random.nextDouble() * 60 - 130);

                String perfData = String.format("Current Airspeed: %d knots\n" +
                                                "Current Altitude: %d ft\n" +
                                                "Fuel Remaining: %d lbs\n" +
                                                "Estimated Fuel at Destination: 6,500 lbs\n" +
                                                "Gross Weight: 150,000 lbs\n" +
                                                "Temperature: -40°C", newSpeed, newAltitude, newFuel);

                String navData = String.format("%s\n" +
                                               "Next Waypoint: WAYPOINT2\n" +
                                               "Distance to Next Waypoint: 150 NM\n" +
                                               "Estimated Time of Arrival: 12:34 UTC", navPosition);

                String weatherData = String.format("Current Weather: %s\n" +
                                                   "Wind: %d° at %d knots\n" +
                                                   "Temperature: %d°C\n" +
                                                   "Visibility: 10 miles", 
                                                   randomChoice(new String[]{"Clear", "Cloudy", "Rainy", "Stormy"}),
                                                   random.nextInt(361), random.nextInt(31), random.nextInt(81) - 40);

                String trafficData = String.format("Traffic: %s\n" +
                                                   "Nearest Aircraft: %d NM\n" +
                                                   "TCAS Status: Normal", 
                                                   randomChoice(new String[]{"No Conflict", "Traffic Alert", "Collision Warning"}),
                                                   random.nextInt(10) + 1);

                perfDataTextArea.setText(perfData);
                navDataTextArea.setText(navData);
                weatherDataTextArea.setText(weatherData);
                trafficDataTextArea.setText(trafficData);
            });
        }, 0, 5, TimeUnit.SECONDS);
    }

    private String randomChoice(String[] options) {
        return options[random.nextInt(options.length)];
    }

    public static void main(String[] args) {
        launch(args);
    }
}
