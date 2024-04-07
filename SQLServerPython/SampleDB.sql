USE [master]
GO
/****** Object: Database [SampleDB] ******/
CREATE DATABASE [SampleDB];
GO
ALTER DATABASE [SampleDB] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [SampleDB].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [SampleDB] SET ANSI_NULL_DEFAULT OFF
GO
ALTER DATABASE [SampleDB] SET ANSI_NULLS OFF
GO
ALTER DATABASE [SampleDB] SET ANSI_PADDING OFF
GO
ALTER DATABASE [SampleDB] SET ANSI_WARNINGS OFF
GO
ALTER DATABASE [SampleDB] SET ARITHABORT OFF
GO
ALTER DATABASE [SampleDB] SET AUTO_CLOSE OFF
GO
ALTER DATABASE [SampleDB] SET AUTO_SHRINK OFF
GO
ALTER DATABASE [SampleDB] SET AUTO_UPDATE_STATISTICS ON
GO
ALTER DATABASE [SampleDB] SET CURSOR_CLOSE_ON_COMMIT OFF
GO
ALTER DATABASE [SampleDB] SET CURSOR_DEFAULT GLOBAL
GO
ALTER DATABASE [SampleDB] SET CONCAT_NULL_YIELDS_NULL OFF
GO
ALTER DATABASE [SampleDB] SET NUMERIC_ROUNDABORT OFF
GO
ALTER DATABASE [SampleDB] SET QUOTED_IDENTIFIER OFF
GO
ALTER DATABASE [SampleDB] SET RECURSIVE_TRIGGERS OFF
GO
ALTER DATABASE [SampleDB] SET DISABLE_BROKER
GO
ALTER DATABASE [SampleDB] SET AUTO_UPDATE_STATISTICS_ASYNC OFF
GO
ALTER DATABASE [SampleDB] SET DATE_CORRELATION_OPTIMIZATION OFF
GO
ALTER DATABASE [SampleDB] SET TRUSTWORTHY OFF
GO
ALTER DATABASE [SampleDB] SET ALLOW_SNAPSHOT_ISOLATION OFF
GO
ALTER DATABASE [SampleDB] SET PARAMETERIZATION SIMPLE
GO
ALTER DATABASE [SampleDB] SET READ_COMMITTED_SNAPSHOT OFF
GO
ALTER DATABASE [SampleDB] SET HONOR_BROKER_PRIORITY OFF
GO
ALTER DATABASE [SampleDB] SET RECOVERY SIMPLE
GO
ALTER DATABASE [SampleDB] SET MULTI_USER
GO
ALTER DATABASE [SampleDB] SET PAGE_VERIFY CHECKSUM
GO
ALTER DATABASE [SampleDB] SET DB_CHAINING OFF
GO
ALTER DATABASE [SampleDB] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF )
GO
ALTER DATABASE [SampleDB] SET TARGET_RECOVERY_TIME = 60 SECONDS
GO
ALTER DATABASE [SampleDB] SET DELAYED_DURABILITY = DISABLED
GO
ALTER DATABASE [SampleDB] SET ACCELERATED_DATABASE_RECOVERY = OFF
GO
EXEC sys.sp_db_vardecimal_storage_format N'SampleDB', N'ON'
GO
ALTER DATABASE [SampleDB] SET QUERY_STORE = OFF
GO
USE [SampleDB]
GO
/****** Object: Table [dbo].[tblCustomers] ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tblCustomers](
[id] [int] NOT NULL,
[code] [varchar](50) NULL,
[firstName] [varchar](50) NULL,
[lastName] [varchar](50) NULL,
PRIMARY KEY CLUSTERED
(
[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON,
ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
INSERT [dbo].[tblCustomers] ([id], [code], [firstName], [lastName]) VALUES (1, N'code1', N'firstName1',
N'lastName1')
INSERT [dbo].[tblCustomers] ([id], [code], [firstName], [lastName]) VALUES (2, N'code2', N'firstName2',
N'lastName2')
INSERT [dbo].[tblCustomers] ([id], [code], [firstName], [lastName]) VALUES (3, N'code3', N'firstName3',
N'lastName3')
INSERT [dbo].[tblCustomers] ([id], [code], [firstName], [lastName]) VALUES (4, N'code4', N'firstName4',
N'lastName4')
INSERT [dbo].[tblCustomers] ([id], [code], [firstName], [lastName]) VALUES (5, N'code5', N'firstName5',
N'lastName5')
GO
USE [master]
GO
ALTER DATABASE [SampleDB] SET READ_WRITE
GO