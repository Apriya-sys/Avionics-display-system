import javafx.application.Application;
import javafx.application.Platform;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.stage.Stage;

import java.util.Random;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

public class MFDDisplay extends Application {

    private final Random random = new Random();

    private Label altitudeLabel;
    private Label speedLabel;
    private Label headingLabel;
    private Label engineTempLabel;
    private Label fuelFlowLabel;
    private Label navigationLabel;
    private Label weatherLabel;
    private Label trafficLabel;

    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("Multi-Function Display (MFD)");

        GridPane grid = createGridPane();

        Scene scene = new Scene(grid, 800, 600, Color.BLACK);
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

        // Flight Data Frame
        HBox flightDataFrame = createFrame();
        altitudeLabel = createLabel("Altitude: 0 ft", "cyan");
        speedLabel = createLabel("Speed: 0 knots", "lime");
        headingLabel = createLabel("Heading: N/A", "yellow");
        flightDataFrame.getChildren().addAll(altitudeLabel, speedLabel, headingLabel);
        grid.add(flightDataFrame, 0, 0);

        // Engine Monitoring Frame
        HBox engineFrame = createFrame();
        engineTempLabel = createLabel("Engine Temp: 0 °C", "orange");
        fuelFlowLabel = createLabel("Fuel Flow: 0 lb/hr", "red");
        engineFrame.getChildren().addAll(engineTempLabel, fuelFlowLabel);
        grid.add(engineFrame, 1, 0);

        // Navigation Frame
        HBox navigationFrame = createFrame();
        navigationLabel = createLabel("Navigation: N/A", "yellow");
        navigationFrame.getChildren().add(navigationLabel);
        grid.add(navigationFrame, 0, 1, 2, 1);

        // Weather Frame
        HBox weatherFrame = createFrame();
        weatherLabel = createLabel("Weather: Clear", "blue");
        weatherFrame.getChildren().add(weatherLabel);
        grid.add(weatherFrame, 0, 2);

        // Traffic Frame
        HBox trafficFrame = createFrame();
        trafficLabel = createLabel("Traffic: No Conflict", "white");
        trafficFrame.getChildren().add(trafficLabel);
        grid.add(trafficFrame, 1, 2);

        return grid;
    }

    private HBox createFrame() {
        HBox frame = new HBox();
        frame.setPadding(new Insets(10));
        frame.setStyle("-fx-border-color: gray; -fx-border-width: 2; -fx-background-color: black;");
        frame.setSpacing(10);
        return frame;
    }

    private Label createLabel(String text, String color) {
        Label label = new Label(text);
        label.setTextFill(Color.web(color));
        label.setFont(Font.font("Helvetica", 20));
        return label;
    }

    private void updateData() {
        ScheduledExecutorService executor = Executors.newScheduledThreadPool(1);
        executor.scheduleAtFixedRate(() -> {
            Platform.runLater(() -> {
                altitudeLabel.setText("Altitude: " + getAltitude() + " ft");
                speedLabel.setText("Speed: " + getSpeed() + " knots");
                headingLabel.setText("Heading: " + getHeading());
                engineTempLabel.setText("Engine Temp: " + getEngineTemp() + " °C");
                fuelFlowLabel.setText("Fuel Flow: " + getFuelFlow() + " lb/hr");
                navigationLabel.setText("Navigation: " + getNavigationData());
                weatherLabel.setText("Weather: " + getWeather());
                trafficLabel.setText("Traffic: " + getTraffic());
            });
        }, 0, 1, TimeUnit.SECONDS);
    }

    private int getAltitude() {
        return random.nextInt(39001) + 1000;
    }

    private int getSpeed() {
        return random.nextInt(401) + 200;
    }

    private String getHeading() {
        String[] headings = {"North", "South", "East", "West", "Northeast", "Northwest", "Southeast", "Southwest"};
        return headings[random.nextInt(headings.length)];
    }

    private int getEngineTemp() {
        return random.nextInt(51) + 50;
    }

    private int getFuelFlow() {
        return random.nextInt(2501) + 500;
    }

    private String getNavigationData() {
        String[] directions = {"Waypoint 1", "Waypoint 2", "Waypoint 3", "Waypoint 4"};
        return directions[random.nextInt(directions.length)];
    }

    private String getWeather() {
        String[] weatherConditions = {"Clear", "Cloudy", "Rainy", "Stormy"};
        return weatherConditions[random.nextInt(weatherConditions.length)];
    }

    private String getTraffic() {
        String[] trafficConditions = {"No Conflict", "Traffic Alert", "Collision Warning"};
        return trafficConditions[random.nextInt(trafficConditions.length)];
    }

    public static void main(String[] args) {
        launch(args);
    }
}
