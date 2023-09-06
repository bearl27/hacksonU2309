package com.example.hacksonu;

import android.os.Bundle;
import androidx.activity.ComponentActivity;
import androidx.compose.runtime.Composable;
import androidx.compose.ui.tooling.preview.Preview;
import com.example.hacksonu.ui.theme.HacksonUTheme;
import androidx.compose.ui.Modifier;
import androidx.compose.material3.Text;
import androidx.compose.material3.MaterialTheme;
import androidx.compose.material3.Surface;
import androidx.compose.foundation.layout.fillMaxSize;

public class MainActivity extends ComponentActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContent(() -> {
            HacksonUThemeKt.HacksonUTheme(() -> {
                SurfaceKt.Surface(
                        ModifierKt.fillMaxSize(),
                        MaterialTheme.colorScheme.getBackground(),
                        () -> {
                            Greeting("Android", ModifierKt.Companion.getDefault());
                            return null;
                        }
                );
                return null;
            });
        });
    }

    @Composable
    public static void Greeting(String name, Modifier modifier) {
        TextKt.Text("Hello " + name + "!", modifier);
    }

    @Preview(showBackground = true)
    @Composable
    public static void GreetingPreview() {
        HacksonUThemeKt.HacksonUTheme(() -> {
            Greeting("Android", ModifierKt.Companion.getDefault());
            return null;
        });
    }
}
