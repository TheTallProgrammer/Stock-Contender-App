
# Stock Contender v1.0.0

Stock Contender is a sophisticated stock advising application designed to identify potential investment opportunities using an array of libraries and algorithms. It analyzes various factors to filter the top 15 stocks from each search, subsequently breaking them down to the top 3, and provides users with clear, concise, and data-backed decisions on stock investments.

## Features 🎉

- Data-driven stock selection algorithm
- Top 15 stock filtering from each search
- Comprehensive breakdown to the top 3 stocks
- Robust ranking backed by comprehensive data
- Integration with OpenAI GPT for additional insights and filtering

## Future Features 🚀

I have ambitious plans for Stock Contender. With your support and feedback, I aim to make it the go-to application for stock advising. Here's a sneak peek into what's in store:

- **Secure User Authentication:** I understand the importance of security and convenience. In an upcoming update, I plan to introduce a login screen that will store user credentials securely in a remote SQL database. This feature will also offer users the option to save their API keys with their credentials for easy access.

- **Expanding User Options:** I'm working on expanding the functionalities available to users. Future updates will offer at least four additional options for contending stocks. These include:

  - **Individual Stock Analysis:** Users will be able to input specific stocks for detailed analysis, providing precise feedback on the investment potential of the selected stocks.
  
  - **Stock Comparer:** Analyze and compare different stocks to understand their performance, growth, and potential.
  
  - **Revolutionary Stock Price Prediction:** I am currently in the process of developing advanced algorithms that will forecast stock price movements based on a plethora of data. This feature is currently a work in progress, and I aim to revolutionize stock prediction with it.
  
  - **Stock of the Day:** A new feature that presents you with the top stock pick of the day, backed by extensive data analysis. This feature will be more data-driven and accurate than the current top 3 stocks due to a significantly larger room for token count.

Stay tuned for these exciting enhancements that will transform your stock advising experience with Stock Contender!

## Prerequisites 📚

To utilize Stock Contender, you must have an OpenAI API Key. This key is essential as the application integrates with the OpenAI GPT model to filter and rank stocks.

### How to Get Your OpenAI API Key

>[Create your OpenAI API key](https://platform.openai.com/account/api-keys) by registering a free account. Please be aware, the API key is displayed just once, so **ensure you save your API key to a local text file for future usage.** If misplaced, a new one will need to be generated.

## Setup and Installation 🛠️

Installing Stock Contender is as simple as executing the application file after the download. Upon running the executable, the application will automatically download the necessary libraries required for its operation - these can be found in the `requirements.txt` file within the installation directory. Should the application prompt for permissions, please accept to proceed. This may take several minutes if it's the first time running the application.

## Usage 💻

After launching the Stock Contender application, you'll be prompted to enter your API key. If you need guidance on how to obtain this key, please refer to the 'How to Get Your OpenAI API Key' section.

Enter your API key by typing it directly into the designated input area, or paste it if you have it copied. Click the 'Activate' button to submit your key. The application will verify your key - if it is accepted, you will be notified. In case of any issues with the key, an error message will be displayed indicating the problem.

With your API key validated, you're ready to begin. Click on the available option to start the analysis process. Stock Contender will then commence its robust data collection and analysis to identify the most promising stocks for investment. 

As the application works its magic, a progress bar will illustrate the ongoing process of data collection and analysis. Upon reaching 100%, the advised stocks will be displayed on the right side of the application. 

Once you have reviewed the output, you can reset the application by clicking the 'Reset and Clear' button. Feel free to repeat the process by clicking on the available option button again for new results. Remember, each analysis by the data-driven AI may yield different stocks - but rest assured, each of them is a solid contender.

## Support 📞 

If you encounter any problems or have questions/ideas, feel free to open an issue, as well as contact me through email, which is listed in the author section below.

## Author 🖋️

Stock Contender is the fruit of dedicated efforts and immense learning. It marks my debut into the world of solo application development.

👤 **Logan Falkenberg**

- Role: Lead Developer, Project Maintainer
- Email: [loganf0101@gmail.com](mailto:loganf0101@gmail.com)
- GitHub: [@TheTallProgrammer](https://github.com/TheTallProgrammer)

I have built this application from the ground up, leveraging the power of Python and incorporating sophisticated libraries and algorithms to provide users with clear, concise, and data-backed decisions on their stock investments. My journey through this project has been both challenging and rewarding, and I am excited to see how it will evolve in the future.

## License 📄

This project is licensed under the MIT License:

Copyright (c) 2023 Logan Falkenberg

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.