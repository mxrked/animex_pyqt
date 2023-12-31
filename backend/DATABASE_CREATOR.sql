USE [Animex]
GO
/****** Object:  Table [dbo].[Anime]    Script Date: 6/12/2023 8:09:22 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Anime](
	[AnimeID] [int] IDENTITY(1,1) NOT NULL,
	[AnimeImg] [nvarchar](max) NULL,
	[AnimeName] [nvarchar](max) NULL,
	[AnimeType] [nvarchar](max) NULL,
	[AnimeYears] [nvarchar](max) NULL,
	[AnimeDesc] [nvarchar](max) NULL,
	[AnimeFavorited] [bit] NULL,
	[AnimeWatched] [bit] NULL,
 CONSTRAINT [PK_Anime] PRIMARY KEY CLUSTERED 
(
	[AnimeID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Products]    Script Date: 6/12/2023 8:09:22 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Products](
	[ProductID] [int] IDENTITY(1,1) NOT NULL,
	[ProductImg] [nvarchar](max) NULL,
	[ProductName] [nvarchar](max) NULL,
	[ProductDesc] [nvarchar](max) NULL,
	[ProductPrice] [nvarchar](max) NULL,
	[ProductQuantity] [nvarchar](max) NULL,
	[ProductFavorited] [bit] NULL,
	[ProductAdded] [bit] NULL,
 CONSTRAINT [PK_Products] PRIMARY KEY CLUSTERED 
(
	[ProductID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Users]    Script Date: 6/12/2023 8:09:22 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Users](
	[UserID] [int] IDENTITY(1,1) NOT NULL,
	[UserEmail] [nvarchar](max) NULL,
	[UserName] [nvarchar](max) NULL,
	[UserPassword] [nvarchar](max) NULL,
	[UserWatchedAnime] [nvarchar](max) NULL,
	[UserFavoritedProducts] [nvarchar](max) NULL,
	[UserFavoritedAnime] [nvarchar](max) NULL,
	[UserCart] [nvarchar](max) NULL,
 CONSTRAINT [PK_Users] PRIMARY KEY CLUSTERED 
(
	[UserID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
