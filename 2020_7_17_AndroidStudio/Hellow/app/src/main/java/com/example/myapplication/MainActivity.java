package com.example.myapplication;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.app.Activity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
public class MainActivity extends AppCompatActivity {
    EditText firstName, lastName, phoneNum;
    TextView player_show_textView, ai_show_textView, game_result_textView;
    String ai_show;
//    private Button btn;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        player_show_textView = (TextView)findViewById(R.id.player_show);
        ai_show_textView = (TextView)findViewById(R.id.AI_show);
        game_result_textView = (TextView)findViewById(R.id.is_win);
    }
    public void onClick(View v)
    {
        switch(v.getId()){
            case R.id.player_stone_button:
                player_show_textView.setText("stone");

                break;
            case R.id.player_scissor_button:
                player_show_textView.setText("scissor");

                break;
            case R.id.player_papper_button:
                player_show_textView.setText("papper");
                break;
        }
        ai_show_textView.setText(computer_ai());
        playerIsWinOrNot();
    }

    public String computer_ai()
    {
        int random_number = (int)(Math.random()* 3);
        switch((int)(Math.random()* 3)){
            case 1:
                ai_show = "stone";
                break;
            case 2:
                ai_show = "scissor";
                break;
            case 3:
                ai_show = "papper";
                break;
            default:
                break;
        }
        return ai_show;
    }

    private void playerIsWinOrNot() {
        if(player_show_textView.getText() == ai_show_textView.getText()){
            game_result_textView.setText("平手");
        }else if(player_show_textView.getText() == "stone" && ai_show_textView.getText() == "scissor" ){
            game_result_textView.setText("你贏了");
        }else if(player_show_textView.getText() == "scissor" && ai_show_textView.getText() == "papper" ){
            game_result_textView.setText("你贏了");
        }else if(player_show_textView.getText() == "papper" && ai_show_textView.getText() == "stone" ){
            game_result_textView.setText("你贏了");
        }else{
            game_result_textView.setText("你輸了");
        }
    }
}
